"""Cache service - stores API responses so we don't have to hit the database every time."""
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()

cache = {}

# A "hit" means the data in the cache
# A "miss" means we did not find it, so we had to query the database
hits = 0
misses = 0


class CacheStore(BaseModel):
    """What the main-api sends us when it wants to store a new response."""
    endpoint: str 
    data: Any


@app.get("/cache")
def get_cache(endpoint: str):
    """Check whether we have a cached response for the given endpoint."""
    global hits, misses

    now = datetime.now()
    cutoff = now - timedelta(minutes=1)

    expired_keys = [key for key, entry in cache.items() if entry["timestamp"] < cutoff]

    for key in expired_keys:
        del cache[key]

    if endpoint in cache:
        hits += 1
        return {"hit": True, "data": cache[endpoint]["data"]}

    misses += 1
    return {"hit": False, "data": None}


@app.post("/cache")
def set_cache(payload: CacheStore):
    """Store a new response in the cache.

    The main-api calls this after it has queried the database,
    so the next identical request can be served from here.
    """
    cache[payload.endpoint] = {
        "data": payload.data,
        "timestamp": datetime.now(),
    }
    return {"message": "Cached"}


@app.get("/log")
def get_log():
    """Return the total number of cache hits and misses since the service started."""
    return {"hits": hits, "misses": misses}
