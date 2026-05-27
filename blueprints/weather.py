"""Backend proxy for OpenWeatherMap current-weather API.

Keeps the API key server-side so it is never exposed to the browser.
Endpoint: GET /api/weather?city=Pune  OR  /api/weather?lat=18.52&lon=73.86
"""
import logging

import requests
from flask import Blueprint, jsonify, request

import config
from blueprints.auth import require_auth

logger = logging.getLogger("agritech.weather")
weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/weather", methods=["GET"])
@require_auth
def get_weather():
    if not config.OPENWEATHER_KEY:
        logger.warning("GET /api/weather called but OPENWEATHER_KEY is not set.")
        return jsonify({"status": "error", "message": "Weather API key not configured.",
            "message": (
                "Open the .env file, set OPENWEATHER_KEY=<your_key>, "
                "then restart the server. "
                "Get a free key at https://openweathermap.org/api"
            ),
        }), 503

    lat = request.args.get("lat")
    lon = request.args.get("lon")
    city = request.args.get("city", "Pune")

    params = {"appid": config.OPENWEATHER_KEY, "units": "metric"}
    if lat and lon:
        params.update({"lat": lat, "lon": lon})
        location_label = f"lat={lat},lon={lon}"
    else:
        params["q"] = city
        location_label = city

    try:
        resp = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params,
            timeout=10,
        )
        resp.raise_for_status()
        logger.info(f"OpenWeatherMap data fetched for: {location_label}")
        return jsonify(resp.json())
    except requests.HTTPError as e:
        status = e.response.status_code
        logger.error(f"OpenWeatherMap HTTP {status} for {location_label}: {e.response.text}")
        if status == 401:
            return jsonify({"status": "error", "message": "Invalid API key. Check OPENWEATHER_KEY in .env."}), 502
        if status == 404:
            return jsonify({"status": "error", "message": f"Location '{city}' not found. Try a different city name."}), 404
        return jsonify({"status": "error", "message": f"Weather API error: {status}"}), 502
    except requests.Timeout:
        logger.warning(f"OpenWeatherMap request timed out for {location_label}")
        return jsonify({"status": "error", "message": "Weather service timed out. Please try again."}), 504
    except Exception as e:
        logger.error(f"Unexpected weather error: {e}", exc_info=True)
        return jsonify({"status": "error", "message": "Unexpected error fetching weather data."}), 500


@weather_bp.route("/weather/forecast", methods=["GET"])
@require_auth
def get_forecast():
    """5-day forecast proxy — OWM key stays server-side."""
    if not config.OPENWEATHER_KEY:
        return jsonify({"status": "error", "message": "Weather API key not configured."}), 503

    city = request.args.get("city", "Pune")
    lat  = request.args.get("lat")
    lon  = request.args.get("lon")

    params = {"appid": config.OPENWEATHER_KEY, "units": "metric", "cnt": 40}
    if lat and lon:
        params.update({"lat": lat, "lon": lon})
        label = f"lat={lat},lon={lon}"
    else:
        params["q"] = city
        label = city

    try:
        resp = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast",
            params=params, timeout=10
        )
        resp.raise_for_status()
        logger.info(f"OWM forecast fetched for: {label}")
        return jsonify(resp.json())
    except requests.HTTPError as e:
        status = e.response.status_code
        if status == 401:
            return jsonify({"status": "error", "message": "Invalid API key."}), 502
        if status == 404:
            return jsonify({"status": "error", "message": f"Location '{city}' not found."}), 404
        return jsonify({"status": "error", "message": f"Forecast API error: {status}"}), 502
    except requests.Timeout:
        return jsonify({"status": "error", "message": "Forecast service timed out."}), 504
    except Exception as e:
        logger.error(f"Forecast error: {e}", exc_info=True)
        return jsonify({"status": "error", "message": "Unexpected error."}), 500

