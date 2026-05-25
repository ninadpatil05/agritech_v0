import sqlite3
from contextlib import contextmanager
import config

@contextmanager
def get_db_connection():
    """Context manager for SQLite DB connections with WAL mode enabled."""
    conn = sqlite3.connect(config.DB_PATH)
    try:
        # Enable Write-Ahead Logging for better concurrency
        conn.execute("PRAGMA journal_mode=WAL;")
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
