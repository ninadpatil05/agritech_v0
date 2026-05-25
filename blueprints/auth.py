import sqlite3
from datetime import datetime, timedelta, timezone
import re
from functools import wraps

import bcrypt
import jwt
from flask import Blueprint, jsonify, request, make_response

import config
from extensions import limiter
from blueprints.db import get_db_connection
import logging

logger = logging.getLogger("agritech.auth")
auth_bp = Blueprint("auth", __name__)


def init_db():
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                password_hash BLOB NOT NULL,
                first_name TEXT,
                last_name TEXT,
                phone TEXT,
                created_at TEXT NOT NULL
            )
            """
        )


def issue_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.now(timezone.utc) + timedelta(hours=config.JWT_EXPIRES_HOURS),
    }
    return jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("agritech_token")
        if not token and "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({"status": "error", "message": "Authentication required."}), 401
        
        try:
            payload = jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
            request.user_email = payload["sub"]
        except jwt.ExpiredSignatureError:
            return jsonify({"status": "error", "message": "Token has expired. Please log in again."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"status": "error", "message": "Invalid authentication token."}), 401
            
        return f(*args, **kwargs)
    return decorated


@auth_bp.route("/signup", methods=["POST"])
@limiter.limit("5 per minute")
def signup():
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    first_name = (data.get("first_name") or "").strip() or None
    last_name = (data.get("last_name") or "").strip() or None
    phone = (data.get("phone") or "").strip() or None

    if not email or not password:
        return jsonify({"status": "error", "message": "Email and password are required."}), 400

    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return jsonify({"status": "error", "message": "Invalid email address format."}), 400
    if len(password) < 8:
        return jsonify({"status": "error", "message": "Password must be at least 8 characters."}), 400

    pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    created = datetime.now(timezone.utc).isoformat()

    try:
        with get_db_connection() as conn:
            conn.execute(
                """
                INSERT INTO users (email, password_hash, first_name, last_name, phone, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (email, pw_hash, first_name, last_name, phone, created),
            )
    except sqlite3.IntegrityError:
        return jsonify({"status": "error", "message": "An account with this email already exists."}), 409
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    token = issue_token(email)
    resp = make_response(jsonify({"message": "User created successfully", "status": "success"}))
    resp.set_cookie("agritech_token", token, httponly=True, secure=False, samesite="Strict")
    resp.set_cookie("logged_in", "1", httponly=False, secure=False, samesite="Strict")
    return resp, 201


@auth_bp.route("/login", methods=["POST"])
@limiter.limit("10 per minute")
def login():
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email or not password:
        return jsonify({"status": "error", "message": "Email and password are required."}), 400

    with get_db_connection() as conn:
        row = conn.execute(
            "SELECT password_hash FROM users WHERE email = ? COLLATE NOCASE",
            (email,),
        ).fetchone()

    if not row:
        logger.warning(f"Failed login attempt (email not found) for email: {email}")
        return jsonify({"status": "error", "message": "Invalid email or password."}), 401

    stored = row[0]
    if isinstance(stored, str):
        stored = stored.encode("utf-8")

    if not bcrypt.checkpw(password.encode("utf-8"), stored):
        logger.warning(f"Failed login attempt (wrong password) for email: {email}")
        return jsonify({"status": "error", "message": "Invalid email or password."}), 401

    token = issue_token(email)
    resp = make_response(jsonify({
        "message": "Login successful",
        "status": "success",
        "token": token,
    }))
    resp.set_cookie("agritech_token", token, httponly=True, secure=False, samesite="Strict")
    resp.set_cookie("logged_in", "1", httponly=False, secure=False, samesite="Strict")
    return resp, 200

@auth_bp.route("/me", methods=["GET"])
@require_auth
def get_me():
    with get_db_connection() as conn:
        row = conn.execute(
            "SELECT id, email, first_name, last_name, phone FROM users WHERE email = ? COLLATE NOCASE",
            (request.user_email,)
        ).fetchone()
    
    if not row:
        return jsonify({"status": "error", "message": "User not found."}), 404
        
    return jsonify({
        "status": "success",
        "user": {
            "id": row[0],
            "email": row[1],
            "first_name": row[2] or "",
            "last_name": row[3] or "",
            "phone": row[4] or ""
        }
    }), 200

@auth_bp.route("/me", methods=["PUT"])
@require_auth
def update_me():
    data = request.get_json(silent=True) or {}
    first_name = (data.get("first_name") or "").strip() or None
    last_name = (data.get("last_name") or "").strip() or None
    phone = (data.get("phone") or "").strip() or None

    if first_name is not None and len(first_name) > 100:
        return jsonify({"status": "error", "message": "first_name must be 100 characters or fewer."}), 400
    if last_name is not None and len(last_name) > 100:
        return jsonify({"status": "error", "message": "last_name must be 100 characters or fewer."}), 400
    if phone is not None and not re.match(r'^\+?[\d\s\-().]{7,20}$', phone):
        return jsonify({"status": "error", "message": "Invalid phone number format."}), 400

    with get_db_connection() as conn:
        conn.execute(
            """
            UPDATE users SET first_name = ?, last_name = ?, phone = ?
            WHERE email = ? COLLATE NOCASE
            """,
            (first_name, last_name, phone, request.user_email),
        )
        row = conn.execute(
            "SELECT id, email, first_name, last_name, phone FROM users WHERE email = ? COLLATE NOCASE",
            (request.user_email,),
        ).fetchone()

    if not row:
        return jsonify({"status": "error", "message": "User not found."}), 404

    return jsonify({
        "status": "success",
        "message": "Profile updated successfully.",
        "user": {
            "id": row[0],
            "email": row[1],
            "first_name": row[2] or "",
            "last_name": row[3] or "",
            "phone": row[4] or ""
        }
    }), 200


@auth_bp.route("/change-password", methods=["PUT"])
@require_auth
def change_password():
    data = request.get_json(silent=True) or {}
    current_password = data.get("current_password") or ""
    new_password = data.get("new_password") or ""

    if not current_password or not new_password:
        return jsonify({"status": "error", "message": "current_password and new_password are required."}), 400
    if len(new_password) < 8:
        return jsonify({"status": "error", "message": "New password must be at least 8 characters."}), 400

    with get_db_connection() as conn:
        row = conn.execute(
            "SELECT password_hash FROM users WHERE email = ? COLLATE NOCASE",
            (request.user_email,),
        ).fetchone()

        if not row:
            return jsonify({"status": "error", "message": "User not found."}), 404

        stored = row[0]
        if isinstance(stored, str):
            stored = stored.encode("utf-8")

        if not bcrypt.checkpw(current_password.encode("utf-8"), stored):
            logger.warning(f"Failed change-password attempt (wrong current password) for email: {request.user_email}")
            return jsonify({"status": "error", "message": "Current password is incorrect."}), 401

        new_hash = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
        conn.execute(
            "UPDATE users SET password_hash = ? WHERE email = ? COLLATE NOCASE",
            (new_hash, request.user_email),
        )

    return jsonify({"status": "success", "message": "Password changed successfully."}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    resp = make_response(jsonify({"status": "success", "message": "Logged out"}))
    resp.set_cookie("agritech_token", "", expires=0)
    resp.set_cookie("logged_in", "", expires=0)
    return resp, 200
