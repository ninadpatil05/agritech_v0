"""
Crop disease detection — Gemini Vision API (REST, no SDK dependency).
Uses a model fallback chain so the first available model wins.
"""
import base64
import io
import json
import logging
import os
import sqlite3

import requests
from flask import Blueprint, jsonify, request
from PIL import Image

import config
from blueprints.disease_db import DISEASE_DB
from blueprints.auth import require_auth

from blueprints.gemini_client import call_gemini, extract_json, GEMINI_MODELS
from blueprints.db import get_db_connection

logger = logging.getLogger("agritech.detection")
detection_bp = Blueprint("detection", __name__)

# ── Disease class list ────────────────────────────────────────────────────────
DISEASE_CLASSES = []
DISEASE_CLASSES_PATH = os.path.join(str(config.MODEL_DIR), "disease_classes.json")

_FALLBACK_CLASSES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust",
    "Apple___healthy", "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew", "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_", "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy", "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot",
    "Peach___healthy", "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
    "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
    "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch", "Strawberry___healthy",
    "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight",
    "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]


def _load_disease_classes():
    global DISEASE_CLASSES
    try:
        if os.path.isfile(DISEASE_CLASSES_PATH):
            with open(DISEASE_CLASSES_PATH, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            if isinstance(loaded, list) and loaded:
                DISEASE_CLASSES = [str(c) for c in loaded]
                return
    except Exception as e:
        logger.warning(f"Could not load disease_classes.json: {e}")
    DISEASE_CLASSES = _FALLBACK_CLASSES[:]


_load_disease_classes()


def _ensure_db():
    try:
        with get_db_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS detections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    disease_class TEXT,
                    confidence REAL,
                    timestamp TEXT
                )
            """)
            try:
                conn.execute("ALTER TABLE detections ADD COLUMN user_id INTEGER")
            except sqlite3.OperationalError:
                pass
            try:
                conn.execute("ALTER TABLE detections ADD COLUMN crop_type TEXT")
            except sqlite3.OperationalError:
                pass
    except Exception as e:
        logger.warning(f"DB init failed: {e}")


_ensure_db()

# ── Helpers ───────────────────────────────────────────────────────────────────

def parse_class_name(class_name: str) -> tuple:
    if "___" in class_name:
        parts = class_name.split("___", 1)
        crop = parts[0].replace("_", " ").replace(",", "").strip()
        disease = parts[1].replace("_", " ").strip().title()
        if "healthy" in disease.lower():
            disease = "Healthy (No Disease)"
        return crop, disease
    return "Unknown", class_name.replace("_", " ").title()


def _to_jpeg(img: Image.Image, max_px: int = 1024) -> bytes:
    img = img.convert("RGB")
    if max(img.size) > max_px:
        img.thumbnail((max_px, max_px), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85, optimize=True)
    return buf.getvalue()


# ── Gemini REST call with model fallback ──────────────────────────────────────

_PROMPT = """\
You are an expert agricultural plant disease detection AI (PlantVillage dataset).

CRITICAL FIRST STEP — Is this image a photo of a crop leaf or plant?
- If the image does NOT show a crop, plant, or leaf (e.g. it is a person, animal, object,
  landscape, food, selfie, or anything non-plant), you MUST set "is_plant": false and leave
  all other fields as empty strings / 0.0. Do NOT guess a class for non-plant images.
- Only proceed to identify a disease class if the image clearly shows a plant/crop leaf.

If it IS a plant image, choose the single closest match from the list below:
{classes}

Respond with VALID JSON ONLY (no markdown, no preamble):
{{
  "is_plant": <true|false>,
  "raw_class": "<exact class string from the list, or empty string if not a plant>",
  "crop_type": "<human-readable crop name, or empty string if not a plant>",
  "disease_name": "<human-readable disease name, or empty string if not a plant>",
  "confidence": <0.0-1.0, use 0.0 if not a plant>,
  "description": "<2-3 sentences about visible symptoms, or empty string if not a plant>"
}}"""


def _call_gemini_detect(jpeg_bytes: bytes, api_key: str) -> tuple:
    classes_str = "\n".join(f"  - {c}" for c in DISEASE_CLASSES)
    prompt = _PROMPT.format(classes=classes_str)
    
    raw_text, model_used = call_gemini(prompt, max_tokens=600, image_bytes=jpeg_bytes)
    return extract_json(raw_text), model_used

# ── Routes ────────────────────────────────────────────────────────────────────

@detection_bp.route("/detect", methods=["POST"])
@require_auth
def detect():
    if "image" not in request.files:
        return jsonify({"status": "error", "message": "No image uploaded"}), 400
    file = request.files["image"]
    if not file or file.filename == "":
        return jsonify({"status": "error", "message": "No image selected"}), 400

    api_key = config.GEMINI_API_KEY
    if not api_key:
        return jsonify({
            "status": "error",
            "error": "GEMINI_API_KEY not set.",
            "message": "Add GEMINI_API_KEY=<your-key> to .env and restart.",
        }), 503

    # Open + convert image
    try:
        img = Image.open(file.stream)
        jpeg_bytes = _to_jpeg(img)
    except Exception as e:
        logger.warning(f"Bad image upload: {e}")
        return jsonify({"status": "error", "message": "Invalid image. Please upload a JPEG or PNG."}), 400

    # Call Gemini
    try:
        analysis, model_used = _call_gemini_detect(jpeg_bytes, api_key)
        logger.info(f"Gemini response ({model_used}): {analysis}")

    except PermissionError as e:
        logger.error(f"Gemini auth error: {e}")
        return jsonify({
            "status": "error",
            "error": str(e),
        }), 403

    except requests.exceptions.HTTPError as e:
        logger.error(f"Gemini HTTP error: {e}")
        return jsonify({"status": "error", "message": f"Gemini API HTTP error: {e}"}), 502

    except requests.exceptions.ConnectionError:
        return jsonify({"status": "error", "message": "Cannot reach Gemini API. Check internet connection."}), 502

    except json.JSONDecodeError:
        return jsonify({"status": "error", "message": "Gemini returned unexpected output. Please retry."}), 500

    except Exception as e:
        logger.error(f"Gemini call failed: {e}", exc_info=True)
        return jsonify({"status": "error", "message": f"Detection failed: {e}"}), 500

    # Plant check — return HTTP 422 so frontend can show a special message
    if not analysis.get("is_plant", True):
        logger.info("Non-plant image submitted — returning 422.")
        return jsonify({
            "status": "not_plant",
            "error": "not_plant",
            "message": (
                "This doesn't look like a crop or plant image. "
                "Please upload a clear, close-up photo of a crop leaf or plant "
                "for accurate disease detection."
            ),
        }), 422

    raw_class  = analysis.get("raw_class", "").strip()
    crop_name  = analysis.get("crop_type", "Unknown")
    disease_name = analysis.get("disease_name", "Unknown")
    confidence = min(max(float(analysis.get("confidence", 0.5)), 0.0), 1.0)
    gemini_desc = analysis.get("description", "")

    # Enrich from disease DB (exact, then loose match)
    report_data = DISEASE_DB.get(raw_class, {})
    if not report_data:
        for key in DISEASE_DB:
            if key.lower().replace("_", "") == raw_class.lower().replace("_", ""):
                report_data = DISEASE_DB[key]
                break

    if not report_data:
        report_data = {
            "crop_type": crop_name,
            "disease": disease_name,
            "description": gemini_desc or f"{disease_name} detected on {crop_name}.",
            "pesticide_treatments": "Use AI Advice for treatment recommendations.",
            "preventive_measures": "Use AI Advice for prevention tips.",
        }

    if "___" in raw_class:
        crop_name, disease_name = parse_class_name(raw_class)

    # Log to DB
    try:
        with get_db_connection() as conn:
            user_row = conn.execute("SELECT id FROM users WHERE email = ? COLLATE NOCASE", (request.user_email,)).fetchone()
            user_id = user_row[0] if user_row else None
            
            conn.execute(
                "INSERT INTO detections (user_id, crop_type, disease_class, confidence, timestamp) "
                "VALUES (?, ?, ?, ?, datetime('now'))",
                (user_id, crop_name[:100], raw_class[:100], confidence),
            )
    except Exception as e:
        logger.warning(f"DB log failed: {e}")

    logger.info(f"Detection OK: {raw_class} ({confidence:.1%}) via {model_used}")
    return jsonify({
        "status": "success",
        "crop_type": crop_name,
        "disease_detected": disease_name,
        "raw_class": raw_class,
        "confidence": confidence,
        "model_used": model_used,
        "report": {
            "disease":                    report_data.get("disease"),
            "description":                report_data.get("description"),
            "causes":                     report_data.get("causes"),
            "soil_requirements":          report_data.get("soil_requirements"),
            "recommended_fertilizers":    report_data.get("recommended_fertilizers"),
            "pesticide_treatments":       report_data.get("pesticide_treatments"),
            "soil_moisture":              report_data.get("soil_moisture"),
            "preventive_measures":        report_data.get("preventive_measures"),
            "additional_recommendations": report_data.get("additional_recommendations"),
        },
    })


@detection_bp.route("/test-gemini", methods=["GET"])
@require_auth
def test_gemini():
    """
    Diagnostic endpoint — hit /api/test-gemini in your browser to see
    exactly which models work with your API key.
    """
    api_key = config.GEMINI_API_KEY
    if not api_key:
        return jsonify({"ok": False, "error": "GEMINI_API_KEY not set in .env"}), 503

    results = {}
    for model in GEMINI_MODELS:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        try:
            resp = requests.post(
                url,
                params={"key": api_key},
                json={"contents": [{"parts": [{"text": "Reply with: ok"}]}],
                      "generationConfig": {"maxOutputTokens": 5}},
                timeout=15,
            )
            if resp.status_code == 200:
                results[model] = "✅ working"
            elif resp.status_code == 404:
                results[model] = "❌ 404 — model not available for your key/plan"
            elif resp.status_code == 403:
                body = resp.text[:200]
                if "allowlist" in body.lower():
                    results[model] = (
                        "❌ 403 — API key has host/IP restrictions. "
                        "Go to https://aistudio.google.com/app/apikey and create "
                        "a new key with NO restrictions."
                    )
                else:
                    results[model] = f"❌ 403 Forbidden: {body}"
            else:
                results[model] = f"❌ {resp.status_code}: {resp.text[:100]}"
        except Exception as e:
            results[model] = f"❌ Exception: {e}"

    working = [m for m, s in results.items() if "✅" in s]
    return jsonify({
        "ok": len(working) > 0,
        "working_models": working,
        "all_results": results,
        "fix_if_all_fail": (
            "Your API key likely has restrictions. "
            "Visit https://aistudio.google.com/app/apikey → Create a new API key "
            "→ choose 'No restriction' → copy the new key → paste it into "
            "your .env as GEMINI_API_KEY=<new_key> → restart Flask."
        ),
    })


@detection_bp.route("/stats", methods=["GET"])
@require_auth
def get_stats():
    try:
        with get_db_connection() as conn:
            cur = conn.cursor()
            
            user_row = cur.execute("SELECT id FROM users WHERE email = ? COLLATE NOCASE", (request.user_email,)).fetchone()
            user_id = user_row[0] if user_row else None
            
            if not user_id:
                return jsonify({
                    "status": "success",
                    "total_scans": 0,
                    "diseases_found": 0,
                    "healthy_plants": 0,
                    "this_week": 0,
                    "total_detections": 0,
                    "top_disease": "N/A",
                    "breakdown": []
                })

            cur.execute("SELECT COUNT(*) FROM detections WHERE user_id = ?", (user_id,))
            total_scans = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM detections WHERE user_id = ? AND disease_class LIKE '%healthy%'", (user_id,))
            healthy_plants = cur.fetchone()[0]

            diseases_found = total_scans - healthy_plants

            cur.execute("SELECT COUNT(*) FROM detections WHERE user_id = ? AND timestamp >= datetime('now', '-7 days')", (user_id,))
            this_week = cur.fetchone()[0]

            cur.execute("""SELECT disease_class, COUNT(*) c FROM detections
                           WHERE user_id = ?
                           GROUP BY disease_class ORDER BY c DESC LIMIT 1""", (user_id,))
            top = cur.fetchone()

            cur.execute("""SELECT disease_class, COUNT(*) c FROM detections
                           WHERE user_id = ?
                           GROUP BY disease_class ORDER BY c DESC LIMIT 5""", (user_id,))
            breakdown = [{"disease_class": r[0], "count": r[1]} for r in cur.fetchall()]
            
            return jsonify({
                "status": "success",
                "total_scans": total_scans,
                "diseases_found": diseases_found,
                "healthy_plants": healthy_plants,
                "this_week": this_week,
                "total_detections": total_scans,
                "top_disease": top[0] if top else "N/A",
                "breakdown": breakdown
            })
    except Exception as e:
        return jsonify({
            "status": "success",
            "total_scans": 0,
            "diseases_found": 0,
            "healthy_plants": 0,
            "this_week": 0,
            "total_detections": 0,
            "top_disease": "N/A",
            "breakdown": [],
            "error": str(e)
        })


@detection_bp.route("/reports", methods=["GET"])
@require_auth
def get_reports():
    try:
        with get_db_connection() as conn:
            user_row = conn.execute("SELECT id FROM users WHERE email = ? COLLATE NOCASE", (request.user_email,)).fetchone()
            if not user_row:
                return jsonify({"status": "success", "reports": []}), 200
                
            rows = conn.execute(
                "SELECT id, crop_type, disease_class, confidence, timestamp FROM detections WHERE user_id = ? ORDER BY id DESC",
                (user_row[0],)
            ).fetchall()
            
        reports = []
        for row in rows:
            reports.append({
                "id": row[0],
                "crop_type": row[1] or "Unknown",
                "disease": parse_class_name(row[2])[1] if row[2] else "Unknown",
                "confidence": row[3],
                "date": row[4]
            })
            
        return jsonify({"status": "success", "reports": reports}), 200
    except Exception as e:
        logger.exception(f"Get reports failed: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@detection_bp.route("/reports", methods=["DELETE"])
@require_auth
def clear_all_reports():
    try:
        with get_db_connection() as conn:
            user_row = conn.execute("SELECT id FROM users WHERE email = ? COLLATE NOCASE", (request.user_email,)).fetchone()
            if user_row:
                conn.execute("DELETE FROM detections WHERE user_id = ?", (user_row[0],))
        return jsonify({"status": "success", "message": "All reports cleared."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@detection_bp.route("/reports/<int:report_id>", methods=["DELETE"])
@require_auth
def delete_report(report_id):
    try:
        with get_db_connection() as conn:
            user_row = conn.execute("SELECT id FROM users WHERE email = ? COLLATE NOCASE", (request.user_email,)).fetchone()
            if user_row:
                conn.execute("DELETE FROM detections WHERE id = ? AND user_id = ?", (report_id, user_row[0]))
        return jsonify({"status": "success", "message": "Report deleted."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# ── /history aliases (used by new frontend) ───────────────────────────────────
# The new frontend calls /history instead of /reports, and expects
# predicted_class (raw class string) + confidence + id + timestamp fields.

@detection_bp.route("/history", methods=["GET"])
@require_auth
def get_history():
    try:
        limit = request.args.get("limit", type=int)
        with get_db_connection() as conn:
            user_row = conn.execute(
                "SELECT id FROM users WHERE email = ? COLLATE NOCASE", (request.user_email,)
            ).fetchone()
            if not user_row:
                return jsonify({"status": "success", "history": []}), 200
            query = "SELECT id, disease_class, confidence, timestamp, crop_type FROM detections WHERE user_id = ? ORDER BY id DESC"
            rows = conn.execute(query, (user_row[0],)).fetchall()

        history = []
        for row in rows:
            history.append({
                "id": row[0],
                "predicted_class": row[1] or "Unknown",
                "confidence": row[2],
                "timestamp": row[3],
                "crop_type": row[4] or "Unknown",
            })

        if limit:
            history = history[:limit]

        return jsonify({"status": "success", "history": history}), 200
    except Exception as e:
        logger.exception(f"Get history failed: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@detection_bp.route("/history", methods=["DELETE"])
@require_auth
def clear_history():
    return clear_all_reports()


@detection_bp.route("/history/<int:report_id>", methods=["DELETE"])
@require_auth
def delete_history_item(report_id):
    return delete_report(report_id)


@detection_bp.route("/health", methods=["GET"])
def health():
    gemini_ok = bool(config.GEMINI_API_KEY)
    return jsonify({
        "status": "ok" if gemini_ok else "degraded",
        "engine": "gemini-vision (REST fallback chain)",
        "models_tried": GEMINI_MODELS,
        "gemini_configured": gemini_ok,
        "disease_classes_loaded": len(DISEASE_CLASSES),
        "validator_model": True,
        "disease_model": True,
        "detail": [] if gemini_ok else ["GEMINI_API_KEY missing in .env"],
    })
