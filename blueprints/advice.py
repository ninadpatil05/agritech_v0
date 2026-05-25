"""Gemini-powered crop disease advice — English & Hindi.
Uses the Gemini REST API directly (no SDK) to avoid protobuf conflicts with TensorFlow.
"""
import hashlib
import json
import logging
import time

import requests
from flask import Blueprint, jsonify, request

import config
from blueprints.auth import require_auth

logger = logging.getLogger("agritech.advice")

advice_bp = Blueprint("advice", __name__)

import threading
from blueprints.gemini_client import call_gemini, extract_json

logger = logging.getLogger("agritech.advice")

advice_bp = Blueprint("advice", __name__)

_PROMPT_TEMPLATE = """You are an expert agricultural scientist and crop doctor.
Detected disease: {disease}
Crop type: {crop_type}

Respond ONLY with this exact JSON structure (no markdown, no code fences):
{{
  "english": {{
    "treatment": ["step 1", "step 2", "step 3", "step 4"],
    "prevention": ["tip 1", "tip 2", "tip 3"],
    "urgency": "high"
  }},
  "hindi": {{
    "treatment": ["\u091a\u0930\u0923 1", "\u091a\u0930\u0923 2", "\u091a\u0930\u0923 3", "\u091a\u0930\u0923 4"],
    "prevention": ["\u0938\u0941\u091d\u093e\u0935 1", "\u0938\u0941\u091d\u093e\u0935 2", "\u0938\u0941\u091d\u093e\u0935 3"],
    "urgency": "\u0909\u091a\u094d\u091a"
  }}
}}

Rules:
- urgency must be one of: low/medium/high (English) and \u0915\u092e/\u092e\u0927\u094d\u092f\u092e/\u0909\u091a\u094d\u091a (Hindi)
- treatment: 3-5 actionable steps in simple farmer-friendly language
- prevention: 3-4 preventive tips
- If disease contains 'healthy', provide general care tips instead
- Keep language simple and practical for Indian farmers
"""


def _call_gemini(disease: str, crop_type: str) -> dict:
    # Sanitise raw PlantVillage class names so the model sees clean text
    disease_clean = disease.replace("___", " ").replace("_", " ").strip()
    prompt = _PROMPT_TEMPLATE.format(disease=disease_clean, crop_type=crop_type)
    
    raw_text, _ = call_gemini(prompt, max_tokens=1024)
    return extract_json(raw_text)


# ── In-memory advice cache ────────────────────────────────────────────────────
_advice_cache: dict = {}
_cache_lock = threading.Lock()
CACHE_MAX_SIZE = 100  # max unique disease+crop combinations to cache


def _cache_key(disease: str, crop_type: str) -> str:
    return hashlib.md5(f"{disease.lower()}|{crop_type.lower()}".encode()).hexdigest()


def get_cached_advice(disease: str, crop_type: str) -> dict:
    key = _cache_key(disease, crop_type)
    
    with _cache_lock:
        if key in _advice_cache:
            logger.info(f"Cache hit for: '{disease}' / '{crop_type}'")
            return _advice_cache[key]
            
    try:
        result = _call_gemini(disease, crop_type)
    except Exception as e:
        logger.error(f"Gemini failed for '{disease}': {e}", exc_info=True)
        raise
        
    with _cache_lock:
        if len(_advice_cache) < CACHE_MAX_SIZE:
            _advice_cache[key] = result
            logger.info(f"Cached advice for '{disease}' / '{crop_type}' (cache size: {len(_advice_cache)})")
    return result


@advice_bp.route("/advice", methods=["POST"])
@require_auth
def get_advice():
    body = request.get_json(silent=True) or {}
    disease = str(body.get("disease", "")).strip()[:100]
    crop_type = str(body.get("crop_type", "Unknown")).strip()[:100]

    if not disease:
        return jsonify({"status": "error", "message": "disease field is required"}), 400

    if not config.GEMINI_API_KEY:
        return jsonify({"status": "error", "message": "Gemini API key not configured.",
            "message": (
                "Open the .env file and set GEMINI_API_KEY=your_key_here, "
                "then restart the server."
            ),
        }), 503

    try:
        advice = get_cached_advice(disease, crop_type)
        return jsonify({"status": "success", "advice": advice})
    except requests.HTTPError as e:
        return jsonify({"status": "error", "message": f"Gemini API error: {e.response.status_code}", "detail": e.response.text}), 502
    except json.JSONDecodeError as e:
        return jsonify({"status": "error", "message": "Failed to parse Gemini response as JSON", "detail": str(e)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@advice_bp.route("/advice/clear-cache", methods=["POST"])
@require_auth
def clear_cache():
    with _cache_lock:
        _advice_cache.clear()
    return jsonify({"status": "cache cleared"})
