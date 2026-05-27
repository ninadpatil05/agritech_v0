"""Weather-driven AI farming advisor.

Four features, one blueprint, zero new dependencies:
  1. POST /api/weather-advice          — actionable advice from live weather
  2. POST /api/irrigation-advice       — irrigation decision (irrigate / skip / reduce)
  3. POST /api/crop-planning           — best crop & sowing time for location + season
  4. GET  /api/weather-alerts          — extreme weather alert evaluation

All calls use the same Gemini REST fallback chain already in advice.py,
and the same OpenWeatherMap proxy already in weather.py.
"""

import hashlib
import json
import logging
import time

import requests
from flask import Blueprint, jsonify, request

import config
from blueprints.auth import require_auth

import threading
from blueprints.gemini_client import call_gemini, extract_json

logger = logging.getLogger("agritech.weather_advice")
weather_advice_bp = Blueprint("weather_advice", __name__)

# ── Simple in-memory cache (TTL = 30 min) ────────────────────────────────────
_cache: dict = {}
_cache_lock = threading.Lock()
_CACHE_TTL = 1800  # seconds


def _cache_get(key: str):
    with _cache_lock:
        entry = _cache.get(key)
        if entry and (time.time() - entry["ts"]) < _CACHE_TTL:
            return entry["value"]
    return None


def _cache_set(key: str, value):
    with _cache_lock:
        if len(_cache) > 200:          # prevent unbounded growth
            oldest = min(_cache, key=lambda k: _cache[k]["ts"])
            del _cache[oldest]
        _cache[key] = {"value": value, "ts": time.time()}


def _cache_key(*parts) -> str:
    return hashlib.md5("|".join(str(p) for p in parts).encode()).hexdigest()



# ── OWM proxy helper ──────────────────────────────────────────────────────────

def _fetch_owm(lat=None, lon=None, city=None) -> dict | None:
    """Fetch current weather from OWM via our own proxy route."""
    if not config.OPENWEATHER_KEY:
        return None
    params = {"appid": config.OPENWEATHER_KEY, "units": "metric"}
    if lat and lon:
        params.update({"lat": lat, "lon": lon})
    elif city:
        params["q"] = city
    else:
        return None
    try:
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params, timeout=10
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logger.warning(f"OWM fetch failed: {e}")
        return None


def _weather_summary(w: dict) -> str:
    """Convert OWM response dict into a compact human-readable string for prompts."""
    main = w.get("main", {})
    wind = w.get("wind", {})
    weather_list = w.get("weather", [{}])
    rain = w.get("rain", {}).get("1h", 0)
    clouds = w.get("clouds", {}).get("all", 0)

    return (
        f"Location: {w.get('name', 'Unknown')}, {w.get('sys', {}).get('country', '')}\n"
        f"Temperature: {main.get('temp', '?')}°C (feels like {main.get('feels_like', '?')}°C)\n"
        f"Humidity: {main.get('humidity', '?')}%\n"
        f"Conditions: {weather_list[0].get('description', 'unknown')}\n"
        f"Wind speed: {wind.get('speed', 0)} m/s\n"
        f"Rainfall last 1h: {rain} mm\n"
        f"Cloud cover: {clouds}%\n"
        f"Pressure: {main.get('pressure', '?')} hPa"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# FEATURE 1 — Weather → Actionable Advice
# POST /api/weather-advice
# Body: { "lat": float, "lon": float, "city": str, "crop": str (optional) }
# ═══════════════════════════════════════════════════════════════════════════════

_WEATHER_ADVICE_PROMPT = """You are an expert agricultural advisor for Indian farmers.
Given the current weather conditions below, provide practical farming guidance.

Weather data:
{weather_summary}

Farmer's crop (if provided): {crop}

Respond ONLY with this exact JSON (no markdown, no preamble):
{{
  "summary": "One sentence describing what today's weather means for farming",
  "do_today": ["action 1", "action 2", "action 3"],
  "avoid_today": ["thing to avoid 1", "thing to avoid 2"],
  "spray_window": "good" | "avoid" | "marginal",
  "spray_reason": "Short reason for spray window decision",
  "field_work": "good" | "avoid" | "marginal",
  "field_work_reason": "Short reason",
  "urgency": "normal" | "caution" | "alert"
}}

Rules:
- All advice must be practical for a small Indian farmer
- do_today: 3 specific, actionable steps (not vague)
- spray_window: "avoid" if humidity > 80% or rain > 0 or wind > 6 m/s
- field_work: "avoid" if rain last 1h > 2mm or wind > 10 m/s
- urgency: "alert" if temperature > 40°C or wind > 12 m/s or heavy rain
"""


@weather_advice_bp.route("/weather-advice", methods=["POST"])
@require_auth
def get_weather_advice():
    body = request.get_json(silent=True) or {}
    lat = body.get("lat")
    lon = body.get("lon")
    city = body.get("city", "").strip()[:100]
    crop = body.get("crop", "general crop").strip()[:100] or "general crop"

    temp = body.get("temperature") or body.get("temp")
    humidity = body.get("humidity")
    description = body.get("description") or body.get("desc")
    wind_speed = body.get("wind_speed") or body.get("wind")

    direct_weather_provided = temp is not None and humidity is not None

    if not (lat and lon) and not city and not direct_weather_provided:
        return jsonify({"status": "error", "message": "Provide lat+lon, city, or direct weather parameters"}), 400

    if not config.GEMINI_API_KEY:
        return jsonify({"status": "error", "message": "GEMINI_API_KEY not configured"}), 503

    # Cache key
    ck_parts = []
    if lat and lon:
        try:
            ck_parts.extend([round(float(lat), 2), round(float(lon), 2)])
        except (ValueError, TypeError):
            ck_parts.extend([lat, lon])
    elif city:
        ck_parts.append(city.lower())
    else:
        ck_parts.extend([temp, humidity])
    ck_parts.append(crop.lower())

    ck = _cache_key(*ck_parts)
    cached = _cache_get(ck)
    if cached:
        logger.info("weather_advice: cache hit")
        return jsonify({"status": "success", "advice": cached, "cached": True})

    weather = None
    if (lat and lon) or city:
        weather = _fetch_owm(lat=lat, lon=lon, city=city)

    if not weather:
        if direct_weather_provided:
            weather = {
                "name": city or "Your Location",
                "main": {
                    "temp": temp,
                    "feels_like": body.get("feels_like") or temp,
                    "humidity": humidity,
                    "pressure": body.get("pressure", 1013)
                },
                "weather": [{"description": description or "clear sky", "icon": body.get("icon") or "01d"}],
                "wind": {"speed": wind_speed or 0},
                "rain": {"1h": body.get("rain_1h") or 0},
                "clouds": {"all": body.get("clouds") or 0},
                "sys": {"country": "IN"}
            }
        else:
            return jsonify({"status": "error", "message": "Could not fetch weather data. Check OPENWEATHER_KEY."}), 502

    prompt = _WEATHER_ADVICE_PROMPT.format(
        weather_summary=_weather_summary(weather),
        crop=crop
    )

    try:
        raw, _ = call_gemini(prompt)
        advice = extract_json(raw)
    except json.JSONDecodeError as e:
        return jsonify({"status": "error", "message": "Gemini returned invalid JSON", "detail": str(e)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    # Attach current weather snapshot for the frontend
    advice["weather_snapshot"] = {
        "temp": weather.get("main", {}).get("temp"),
        "humidity": weather.get("main", {}).get("humidity"),
        "wind_speed": weather.get("wind", {}).get("speed"),
        "description": weather.get("weather", [{}])[0].get("description", ""),
        "location": weather.get("name", city or f"{lat},{lon}"),
    }

    _cache_set(ck, advice)
    return jsonify({"status": "success", "advice": advice})


# ═══════════════════════════════════════════════════════════════════════════════
# FEATURE 2 — Irrigation Optimization
# POST /api/irrigation-advice
# Body: { "lat": float, "lon": float, "city": str, "crop": str,
#         "soil_type": str (optional), "crop_stage": str (optional) }
# ═══════════════════════════════════════════════════════════════════════════════

_IRRIGATION_PROMPT = """You are an expert irrigation advisor for Indian farmers.

Current weather:
{weather_summary}

Crop: {crop}
Soil type: {soil_type}
Crop growth stage: {crop_stage}

Based on the weather, decide the optimal irrigation action for today.

Respond ONLY with this exact JSON (no markdown, no preamble):
{{
  "decision": "irrigate" | "skip" | "reduce",
  "confidence": "high" | "medium" | "low",
  "reason": "2-3 sentences explaining the decision in simple language",
  "timing": "Best time to irrigate if recommended (e.g. 'Early morning 5-7 AM')",
  "amount": "Suggested water amount (e.g. '25mm' or 'skip today')",
  "next_check": "When to re-evaluate (e.g. 'Check again tomorrow morning')",
  "water_saving_tip": "One practical tip to save water for this crop and weather"
}}

Rules:
- decision "skip" if: rainfall last 1h > 5mm OR humidity > 85% OR rain_probability > 70%
- decision "reduce" if: recent rain 2-5mm OR humidity 75-85%
- decision "irrigate" if: no rain + humidity < 70% + temperature > 30°C
- For sandy soil: recommend more frequent but smaller amounts
- For clay soil: recommend less frequent but deeper irrigation
- timing: always prefer early morning (before 8 AM) or evening (after 6 PM) to minimize evaporation
"""


@weather_advice_bp.route("/irrigation-advice", methods=["POST"])
def irrigation_advice():
    body = request.get_json(silent=True) or {}
    lat = body.get("lat")
    lon = body.get("lon")
    city = body.get("city", "").strip()[:100]
    crop = body.get("crop", "general crop").strip()[:100] or "general crop"
    soil_type = body.get("soil_type", "loam").strip()[:100] or "loam"
    crop_stage = body.get("crop_stage", "vegetative").strip()[:100] or "vegetative"

    if not (lat and lon) and not city:
        return jsonify({"status": "error", "message": "Provide lat+lon or city"}), 400

    if not config.GEMINI_API_KEY:
        return jsonify({"status": "error", "message": "GEMINI_API_KEY not configured"}), 503

    ck = _cache_key(
        round(float(lat), 2) if lat else city.lower(),
        crop.lower(), soil_type.lower(), crop_stage.lower()
    )
    cached = _cache_get(ck)
    if cached:
        return jsonify({"status": "success", "irrigation": cached, "cached": True})

    weather = _fetch_owm(lat=lat, lon=lon, city=city)
    if not weather:
        return jsonify({"status": "error", "message": "Could not fetch weather data. Check OPENWEATHER_KEY."}), 502

    prompt = _IRRIGATION_PROMPT.format(
        weather_summary=_weather_summary(weather),
        crop=crop,
        soil_type=soil_type,
        crop_stage=crop_stage
    )

    try:
        raw, _ = call_gemini(prompt, max_tokens=512)
        result = extract_json(raw)
    except json.JSONDecodeError as e:
        return jsonify({"status": "error", "message": "Gemini returned invalid JSON", "detail": str(e)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    result["location"] = weather.get("name", city or f"{lat},{lon}")
    _cache_set(ck, result)
    return jsonify({"status": "success", "irrigation": result})


# ═══════════════════════════════════════════════════════════════════════════════
# FEATURE 3 — Smart Crop Planning
# POST /api/crop-planning
# Body: { "lat": float, "lon": float, "city": str,
#         "land_size_acres": float (optional), "soil_type": str (optional),
#         "available_water": str (optional) }
# ═══════════════════════════════════════════════════════════════════════════════

_CROP_PLANNING_PROMPT = """You are an expert agricultural scientist advising a small Indian farmer.

Current weather and location data:
{weather_summary}

Farmer's details:
- Land size: {land_size} acres
- Soil type: {soil_type}
- Water availability: {available_water}

Based on the current season, location, and weather trends, recommend the best crops to grow.

Respond ONLY with this exact JSON (no markdown, no preamble):
{{
  "season": "Current season name (e.g. Kharif 2025, Rabi 2025-26)",
  "top_crops": [
    {{
      "name": "Crop name",
      "suitability": "excellent" | "good" | "moderate",
      "reason": "Why this crop suits current conditions",
      "sowing_window": "Best sowing period (e.g. 'June 15 - July 10')",
      "expected_yield": "Expected yield per acre (e.g. '15-18 quintals/acre')",
      "water_requirement": "low" | "medium" | "high",
      "market_demand": "high" | "medium" | "low"
    }}
  ],
  "avoid_crops": ["Crop to avoid 1 and why", "Crop to avoid 2 and why"],
  "soil_prep_tip": "One key soil preparation tip for current conditions",
  "best_sowing_date": "Ideal sowing date window based on current weather"
}}

Rules:
- Recommend 3 top crops ranked by suitability
- Consider current temperature and humidity for crop selection
- Prioritize crops common in India: rice, wheat, cotton, sugarcane, soybean, groundnut,
  onion, tomato, chilli, turmeric, maize, bajra, jowar, pulses
- If temperature > 35°C, prefer heat-tolerant crops
- If humidity > 75%, prefer crops less susceptible to fungal disease
- Give practical, farmer-friendly language
"""


@weather_advice_bp.route("/crop-planning", methods=["POST"])
def crop_planning():
    body = request.get_json(silent=True) or {}
    lat = body.get("lat")
    lon = body.get("lon")
    city = body.get("city", "").strip()[:100]
    land_size = body.get("land_size_acres", 2)
    soil_type = body.get("soil_type", "loam").strip()[:100] or "loam"
    available_water = body.get("available_water", "canal + borewell").strip()[:100] or "canal + borewell"

    if not (lat and lon) and not city:
        return jsonify({"status": "error", "message": "Provide lat+lon or city"}), 400

    if not config.GEMINI_API_KEY:
        return jsonify({"status": "error", "message": "GEMINI_API_KEY not configured"}), 503

    ck = _cache_key(
        round(float(lat), 1) if lat else city.lower(),
        soil_type.lower(), available_water.lower()
    )
    cached = _cache_get(ck)
    if cached:
        return jsonify({"status": "success", "plan": cached, "cached": True})

    weather = _fetch_owm(lat=lat, lon=lon, city=city)
    if not weather:
        return jsonify({"status": "error", "message": "Could not fetch weather data. Check OPENWEATHER_KEY."}), 502

    prompt = _CROP_PLANNING_PROMPT.format(
        weather_summary=_weather_summary(weather),
        land_size=land_size,
        soil_type=soil_type,
        available_water=available_water
    )

    try:
        raw, _ = call_gemini(prompt, max_tokens=1200)
        plan = extract_json(raw)
    except json.JSONDecodeError as e:
        return jsonify({"status": "error", "message": "Gemini returned invalid JSON", "detail": str(e)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    plan["location"] = weather.get("name", city or f"{lat},{lon}")
    _cache_set(ck, plan)
    return jsonify({"status": "success", "plan": plan})


# ═══════════════════════════════════════════════════════════════════════════════
# FEATURE 4 — Extreme Weather Alerts
# GET /api/weather-alerts?lat=&lon=  OR  ?city=
# ═══════════════════════════════════════════════════════════════════════════════

# Thresholds for automatic rule-based alerts (no Gemini needed — fast & free)
_ALERT_RULES = [
    {"field": "main.temp",       "op": "gte", "value": 42,  "level": "red",    "title": "Extreme heat",      "msg": "Temperature is {val}°C — dangerously high. Stop field work after 9 AM. Keep crops hydrated. Protect livestock."},
    {"field": "main.temp",       "op": "gte", "value": 38,  "level": "orange", "title": "Heat stress",       "msg": "Temperature is {val}°C — heat stress risk. Irrigate early morning, mulch soil."},
    {"field": "main.temp",       "op": "lte", "value": 10,  "level": "orange", "title": "Cold stress",       "msg": "Temperature is {val}°C — cold stress for most crops. Cover seedlings overnight."},
    {"field": "wind.speed",      "op": "gte", "value": 15,  "level": "red",    "title": "Strong wind",       "msg": "Wind at {val} m/s — suspend all spraying. Secure crop covers and greenhouse nets."},
    {"field": "wind.speed",      "op": "gte", "value": 8,   "level": "orange", "title": "Elevated wind",     "msg": "Wind at {val} m/s — avoid pesticide spraying. Use drift-reduction nozzles if spraying is essential."},
    {"field": "main.humidity",   "op": "gte", "value": 90,  "level": "orange", "title": "Very high humidity","msg": "Humidity at {val}% — high fungal disease risk. Inspect crops and improve ventilation."},
    {"field": "rain.1h",         "op": "gte", "value": 20,  "level": "red",    "title": "Heavy rainfall",    "msg": "Rainfall {val} mm/hr — check field drainage immediately. Delay fertilizer and spray."},
    {"field": "rain.1h",         "op": "gte", "value": 5,   "level": "orange", "title": "Moderate rain",     "msg": "Rainfall {val} mm/hr — postpone spraying and harvesting. Ensure drainage is clear."},
]


def _nested_get(d: dict, path: str):
    """Get value from nested dict using dot notation. Returns None if missing."""
    keys = path.split(".")
    val = d
    for k in keys:
        if not isinstance(val, dict):
            return None
        val = val.get(k)
    return val


def _evaluate_alerts(weather: dict) -> list:
    alerts = []
    seen_fields = set()  # only highest alert per field

    # Sort rules so higher-value thresholds (more severe) are checked first
    sorted_rules = sorted(_ALERT_RULES, key=lambda r: r["value"], reverse=True)

    for rule in sorted_rules:
        field = rule["field"]
        val = _nested_get(weather, field)
        if val is None:
            continue

        triggered = False
        if rule["op"] == "gte" and val >= rule["value"]:
            triggered = True
        elif rule["op"] == "lte" and val <= rule["value"]:
            triggered = True

        if triggered and field not in seen_fields:
            seen_fields.add(field)
            alerts.append({
                "level": rule["level"],
                "title": rule["title"],
                "message": rule["msg"].replace("{val}", str(round(val, 1))),
                "field": field,
                "value": round(val, 1),
            })

    # Sort: red first, then orange
    alerts.sort(key=lambda a: 0 if a["level"] == "red" else 1)
    return alerts


@weather_advice_bp.route("/weather-alerts", methods=["GET"])
def weather_alerts():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    city = request.args.get("city", "").strip()

    if not (lat and lon) and not city:
        return jsonify({"status": "error", "message": "Provide lat+lon or city query parameter"}), 400

    weather = _fetch_owm(lat=lat, lon=lon, city=city)
    if not weather:
        return jsonify({
            "status": "unavailable",
            "alerts": [],
            "message": "Weather service unavailable. Check OPENWEATHER_KEY.",
        }), 200  # 200 so frontend degrades gracefully

    alerts = _evaluate_alerts(weather)
    location = weather.get("name", city or f"{lat},{lon}")
    country = weather.get("sys", {}).get("country", "")

    return jsonify({
        "status": "success",
        "location": f"{location}, {country}".strip(", "),
        "alert_count": len(alerts),
        "has_critical": any(a["level"] == "red" for a in alerts),
        "alerts": alerts,
        "weather_snapshot": {
            "temp": weather.get("main", {}).get("temp"),
            "humidity": weather.get("main", {}).get("humidity"),
            "wind_speed": weather.get("wind", {}).get("speed"),
            "rain_1h": weather.get("rain", {}).get("1h", 0),
        },
    })


# ── /weather-advisory alias (used by new frontend) ────────────────────────────
@weather_advice_bp.route("/weather-advisory", methods=["POST"])
def weather_advisory_alias():
    """Alias for /weather-advice used by the new frontend."""
    return get_weather_advice()


@weather_advice_bp.route("/weather/chat", methods=["POST"])
@require_auth
def weather_chat():
    """Gemini AI chat proxy — key stays server-side."""
    body = request.get_json(silent=True) or {}
    user_message = body.get("message", "").strip()[:500]
    weather_ctx  = body.get("weather", {})

    if not user_message:
        return jsonify({"status": "error", "message": "No message provided."}), 400
    if not config.GEMINI_API_KEY:
        return jsonify({"status": "error", "message": "GEMINI_API_KEY not configured."}), 503

    weather_str = "Weather data not available."
    if weather_ctx:
        weather_str = (
            f"Location: {weather_ctx.get('name', 'unknown')}, India. "
            f"Temp: {weather_ctx.get('temp', '?')}°C, "
            f"Humidity: {weather_ctx.get('humidity', '?')}%, "
            f"Condition: {weather_ctx.get('description', 'unknown')}, "
            f"Wind: {weather_ctx.get('wind_speed', 0)} km/h."
        )

    prompt = (
        "You are an expert Indian agricultural advisor.\n"
        f"Current weather: {weather_str}\n"
        f"Farmer's question: \"{user_message}\"\n"
        "Give a concise, practical answer in 3-4 sentences for rural Indian farmers. "
        "End with one clear actionable step for today."
    )

    try:
        raw, model = call_gemini(prompt, max_tokens=400)
        return jsonify({"status": "success", "reply": raw.strip(), "model": model})
    except Exception as e:
        logger.error(f"weather_chat error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 502


@weather_advice_bp.route("/weather/crop-recommendations", methods=["POST"])
@require_auth
def crop_recommendations():
    """Crop planning AI proxy — Gemini key stays server-side."""
    body         = request.get_json(silent=True) or {}
    season       = body.get("season", "kharif").strip()[:50]
    land_size    = body.get("land_size", "2 acres").strip()[:50]
    soil_type    = body.get("soil_type", "loam").strip()[:50]
    water_avail  = body.get("water_avail", "canal").strip()[:100]
    city         = body.get("city", "").strip()[:100]
    lat          = body.get("lat")
    lon          = body.get("lon")

    if not config.GEMINI_API_KEY:
        return jsonify({"status": "error", "message": "GEMINI_API_KEY not configured."}), 503

    weather_str = ""
    if (lat and lon) or city:
        w = _fetch_owm(lat=lat, lon=lon, city=city)
        if w:
            weather_str = f"\nCurrent weather:\n{_weather_summary(w)}"

    prompt = (
        f"You are an expert agricultural scientist advising a small Indian farmer.\n"
        f"Season: {season}\nLand: {land_size}\nSoil: {soil_type}\n"
        f"Water: {water_avail}{weather_str}\n\n"
        "Recommend best crops. Respond ONLY with valid JSON, no markdown:\n"
        '{"top_crops":[{"name":str,"suitability":"excellent"|"good"|"moderate",'
        '"reason":str,"sowing_window":str,"water_requirement":"low"|"medium"|"high"}],'
        '"avoid_crops":[str],"soil_prep_tip":str,"season_label":str}'
    )

    try:
        import re as _re
        raw, model = call_gemini(prompt, max_tokens=1200)
        clean  = raw.replace("```json", "").replace("```", "").strip()
        match  = _re.search(r"\{[\s\S]*\}", clean)
        parsed = json.loads(match.group(0) if match else clean)
        return jsonify({"status": "success", "recommendations": parsed, "model": model})
    except Exception as e:
        logger.error(f"crop_recommendations error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 502


