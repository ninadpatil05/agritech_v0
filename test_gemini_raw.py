
import config
from blueprints.gemini_client import call_gemini

prompt = "Reply with valid JSON only: { \"status\": \"ok\" }"
try:
    print("Calling Gemini...")
    raw, model = call_gemini(prompt, max_tokens=100)
    print(f"Model: {model}")
    print(f"Raw: {raw!r}")
except Exception as e:
    print(f"Error: {e}")

