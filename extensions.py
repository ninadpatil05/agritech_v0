from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request
import os

# Set generous limits in debug mode to facilitate developer testing and avoid 429 locks
is_debug = os.environ.get("FLASK_DEBUG", "false").lower() in ("1", "true", "yes")
default_limits = ["10000 per day", "2000 per hour"] if is_debug else ["500 per day", "100 per hour"]

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=default_limits
)

# Exempt localhost connections entirely to prevent developers from getting rate-limited during testing
@limiter.request_filter
def exempt_localhost():
    return request.remote_addr in ("127.0.0.1", "::1", "localhost")
