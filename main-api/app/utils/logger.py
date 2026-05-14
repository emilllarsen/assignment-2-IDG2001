"""Helper for sending log entries to the logger service."""
import httpx

LOGGER_URL = "http://logger:8004"


def log_request(username: str, endpoint: str, tokens: int = 1):
    """Tell the logger service to record a request. Silently ignored if logger is down."""
    try:
        httpx.post(f"{LOGGER_URL}/log", json={
            "username": username,
            "endpoint": endpoint,
            "tokens": tokens,
        })
    except httpx.ConnectError:
        pass
