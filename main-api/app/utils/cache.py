"""Helper functions for talking to the cache service."""
import httpx

# The address of the cache container inside Docker's network
CACHE_URL = "http://cache:8003"


def get_cached(endpoint: str):
    """Ask the cache service if it has a stored response for this endpoint.

    Returns the cached data if found, or none if not found.
    If the cache service is unreachable, we silently return none so the
    main-api just falls back to querying the database as normal.
    """
    try:
        resp = httpx.get(f"{CACHE_URL}/cache", params={"endpoint": endpoint})
        result = resp.json()
        if result["hit"]:
            return result["data"]
    except httpx.ConnectError:
        pass
    return None


def store_cache(endpoint: str, data: dict):
    """Tell the cache service to store a response for this endpoint.

    Called after the main-api has fetched data from the database,
    so the next identical request can come from the cache instead.
    If the cache service is unreachable, we do nothing.
    """
    try:
        httpx.post(f"{CACHE_URL}/cache", json={"endpoint": endpoint, "data": data})
    except httpx.ConnectError:
        pass
