
from blueprints.gemini_client import extract_json
raw = "```json\n{ \"status\": \"ok\" }\n```"
try:
    print(extract_json(raw))
except Exception as e:
    print(f"Error: {e}")

