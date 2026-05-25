import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory, redirect
from flask_cors import CORS

load_dotenv()

# ── Logging setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),              # console
        logging.FileHandler("agritech.log"),  # persistent file
    ],
)
logger = logging.getLogger("agritech")
logger.info("AgriTech server starting up.")

import config
from blueprints.auth import auth_bp, init_db
from blueprints.contact import contact_bp
from blueprints.detection import detection_bp
from blueprints.advice import advice_bp
from blueprints.weather import weather_bp
from blueprints.weather_advice import weather_advice_bp
from extensions import limiter

def create_app():
    app = Flask(__name__, static_folder=".", static_url_path="")
    app.config["SECRET_KEY"] = config.SECRET_KEY
    CORS(app)

    limiter.init_app(app)
    init_db()

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(contact_bp, url_prefix="/api")
    app.register_blueprint(detection_bp, url_prefix="/api")
    app.register_blueprint(advice_bp, url_prefix="/api")
    app.register_blueprint(weather_bp, url_prefix="/api")
    app.register_blueprint(weather_advice_bp, url_prefix="/api")

    @app.before_request
    def enforce_https():
        if request.headers.get("X-Forwarded-Proto") == "http":
            url = request.url.replace("http://", "https://", 1)
            return redirect(url, code=301)

    @app.after_request
    def add_security_headers(response):
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://translate.google.com https://translate.googleapis.com; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://translate.google.com https://translate.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com data:; "
            "img-src 'self' data: blob: https://images.unsplash.com https://translate.google.com https://translate.googleapis.com https://www.gstatic.com https://openweathermap.org; "
            "connect-src 'self' https://api.open-meteo.com https://geocoding-api.open-meteo.com https://translate.google.com https://translate.googleapis.com; "
            "media-src 'self' blob:;"
        )
        response.headers['Content-Security-Policy'] = csp
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response

    @app.route("/")
    def index():
        return send_from_directory(".", "index.html")

    @app.route("/<path:path>")
    def serve_file(path):
        return send_from_directory(".", path)

    @app.errorhandler(404)
    def page_not_found(e):
        return send_from_directory(".", "404.html"), 404

    # ── Admin: tail log file ───────────────────────────────────────
    _LOGS_TOKEN = os.environ.get("LOGS_TOKEN", "admintoken")

    @app.route("/api/logs", methods=["GET"])
    def tail_logs():
        token = request.headers.get("X-Admin-Token", "")
        if token != _LOGS_TOKEN:
            return jsonify({"error": "Forbidden"}), 403
        log_path = os.path.join(os.path.dirname(__file__), "agritech.log")
        try:
            with open(log_path, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
            return jsonify({"lines": [l.rstrip() for l in lines[-50:]]})
        except FileNotFoundError:
            return jsonify({"lines": [], "note": "Log file not yet created."})

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(debug=config.FLASK_DEBUG, port=port)
