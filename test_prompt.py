
import config
from blueprints.gemini_client import call_gemini
from blueprints.detection import _PROMPT, DISEASE_CLASSES
from PIL import Image

classes_str = "\n".join(f"  - {c}" for c in DISEASE_CLASSES)
prompt = _PROMPT.format(classes=classes_str)

img = Image.new("RGB", (224, 224), color = "green")
img.save("dummy.jpg")
with open("dummy.jpg", "rb") as f:
    jpeg_bytes = f.read()

try:
    print("Calling Gemini...")
    raw, model = call_gemini(prompt, max_tokens=600, image_bytes=jpeg_bytes)
    print(f"Model: {model}")
    print(f"Raw: {raw!r}")
except Exception as e:
    print(f"Error: {e}")

