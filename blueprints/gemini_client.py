import json
import logging
import requests
import base64
import config

logger = logging.getLogger("agritech.gemini_client")

# Shared list of fallback models
GEMINI_MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.5-flash",
    "gemini-2.5-flash-preview-05-20",
]
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

import re

def extract_json(text: str) -> dict:
    """Robustly parse a JSON object from Gemini output."""
    text = text.strip()
    # Try parsing the whole thing first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
        
    # Strip markdown code blocks
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:])
        if text.rstrip().endswith("```"):
            text = text.rstrip()[:-3].rstrip()
            
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
        
    # Regex fallback to find anything that looks like a JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass
            
    logger.error(f"Failed to parse JSON from text: {text!r}")
    raise json.JSONDecodeError("Could not extract valid JSON from Gemini output", text, 0)

def call_gemini(prompt: str, max_tokens: int = 1024, image_bytes: bytes = None) -> tuple:
    """Send prompt to Gemini; try each model in the fallback chain.
    Returns (raw text, model_used) or raises Exception."""
    api_key = config.GEMINI_API_KEY
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    from flask import request as flask_req
    lang_instruction = ""
    try:
        lang = flask_req.headers.get("Accept-Language", "en")
        if lang.startswith("hi"):
            lang_instruction = "\n\nIMPORTANT INSTRUCTION: YOU MUST GENERATE ALL TEXT, DESCRIPTIONS, AND ADVICE IN HINDI (हिन्दी). Do not use English for the content."
        elif lang.startswith("mr"):
            lang_instruction = "\n\nIMPORTANT INSTRUCTION: YOU MUST GENERATE ALL TEXT, DESCRIPTIONS, AND ADVICE IN MARATHI (मराठी). Do not use English for the content."
    except Exception:
        pass

    parts = []
    if image_bytes:
        parts.append({"inline_data": {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(image_bytes).decode()
        }})
    parts.append({"text": prompt + lang_instruction})

    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": max_tokens},
    }

    last_err = None
    for model in GEMINI_MODELS:
        url = GEMINI_API_BASE.format(model=model)
        try:
            resp = requests.post(url, params={"key": api_key}, json=payload, timeout=30)
            
            if resp.status_code == 429:
                # 429 rate limit - fail fast, do not sleep in Flask worker
                logger.warning(f"Gemini 429 on {model}, trying next model immediately.")
                last_err = requests.exceptions.HTTPError("429 Too Many Requests", response=resp)
                continue
            
            if resp.status_code == 404:
                logger.warning(f"Gemini model {model} not found, trying next.")
                last_err = Exception(f"{model}: 404 Not Found")
                continue
                
            if resp.status_code == 403:
                body = resp.text[:300]
                if "allowlist" in body.lower() or "not allowed" in body.lower():
                    raise PermissionError("API key has host/IP restrictions. Please create an unrestricted key.")
                raise PermissionError(f"403 Forbidden: {body}")
                
            resp.raise_for_status()
            raw = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
            logger.info(f"Gemini ({model}) responded OK")
            return raw.strip(), model
        except (PermissionError, json.JSONDecodeError, KeyError) as e:
            raise
        except requests.exceptions.RequestException as e:
            last_err = e
            logger.warning(f"Gemini {model} error: {e}")
            continue

    if getattr(last_err, 'response', None) and getattr(last_err.response, 'status_code', None) == 429:
         raise Exception("Gemini rate limit hit on all models. The free tier allows 15 requests/min. Please wait ~1 minute and try again.")
    raise last_err or RuntimeError("All Gemini models failed.")
