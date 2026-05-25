
from PIL import Image
import config
from blueprints.detection import _call_gemini_detect

img = Image.new("RGB", (224, 224), color = "green")
img.save("dummy.jpg")
with open("dummy.jpg", "rb") as f:
    jpeg_bytes = f.read()

try:
    print("Calling Gemini detect...")
    res, model = _call_gemini_detect(jpeg_bytes, config.GEMINI_API_KEY)
    print(f"Model: {model}")
    print(f"Result: {res}")
except Exception as e:
    print(f"Error: {e}")

