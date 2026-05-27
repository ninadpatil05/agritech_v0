#!/usr/bin/env bash
# download_models.sh — Fetches ML model files at Render build time.
# Called from render.yaml buildCommand only if PLANT_MODEL_URL / DISEASE_MODEL_URL are set.
# Models are placed in /tmp/models so the app can find them at runtime.

set -euo pipefail

MODEL_DIR="${MODEL_PATH:-/tmp/models}"
PLANT_FILE="${MODEL_DIR}/plant_validator_model.h5"
DISEASE_FILE="${MODEL_DIR}/crop_disease_model.h5"

echo "=== Smart Crop Detective — Model Bootstrap ==="
echo "Target directory: ${MODEL_DIR}"

mkdir -p "${MODEL_DIR}"

# ── Plant Validator Model ──────────────────────────────────────────
if [ -f "${PLANT_FILE}" ]; then
    echo "[SKIP] plant_validator_model.h5 already exists."
else
    if [ -z "${PLANT_MODEL_URL:-}" ]; then
        echo "[ERROR] PLANT_MODEL_URL is not set and plant_validator_model.h5 is missing."
        echo "        Set PLANT_MODEL_URL to a direct download URL (HuggingFace / Google Drive)."
        exit 1
    fi
    echo "[DOWNLOAD] Fetching plant_validator_model.h5 ..."
    curl -fSL --progress-bar "${PLANT_MODEL_URL}" -o "${PLANT_FILE}" || {
        echo "[ERROR] Failed to download plant_validator_model.h5 from: ${PLANT_MODEL_URL}"
        rm -f "${PLANT_FILE}"
        exit 1
    }
    echo "[OK] plant_validator_model.h5 downloaded ($(du -sh "${PLANT_FILE}" | cut -f1))."
fi

# ── Crop Disease Model ─────────────────────────────────────────────
if [ -f "${DISEASE_FILE}" ]; then
    echo "[SKIP] crop_disease_model.h5 already exists."
else
    if [ -z "${DISEASE_MODEL_URL:-}" ]; then
        echo "[ERROR] DISEASE_MODEL_URL is not set and crop_disease_model.h5 is missing."
        echo "        Set DISEASE_MODEL_URL to a direct download URL (HuggingFace / Google Drive)."
        exit 1
    fi
    echo "[DOWNLOAD] Fetching crop_disease_model.h5 ..."
    curl -fSL --progress-bar "${DISEASE_MODEL_URL}" -o "${DISEASE_FILE}" || {
        echo "[ERROR] Failed to download crop_disease_model.h5 from: ${DISEASE_MODEL_URL}"
        rm -f "${DISEASE_FILE}"
        exit 1
    }
    echo "[OK] crop_disease_model.h5 downloaded ($(du -sh "${DISEASE_FILE}" | cut -f1))."
fi

echo "=== Model bootstrap complete. ==="
