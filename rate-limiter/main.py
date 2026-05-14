"""Rate Limiter - Tracks request frequency per user."""
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage: {user_id: [list of datetime timestamps]}
DATA = {}


class RequestLog(BaseModel):
    """Schema for logging a request."""
    username: str


@app.post("/{user_id}")
def add_request(user_id: str, payload: RequestLog):
    """Log a new request for a user."""
    now = datetime.now()
    if user_id not in DATA:
        DATA[user_id] = []

    DATA[user_id].append(now)

    # Clean out entries older than 10 seconds
    cutoff = now - timedelta(seconds=10)
    DATA[user_id] = [t for t in DATA[user_id] if t > cutoff]

    return {"message": "Request logged"}


@app.get("/{user_id}")
def get_requests(user_id: str):
    """Return request count and delay for a user."""
    now = datetime.now()

    if user_id not in DATA:
        return {"requests": 0, "delay": 0.0}

    # Clean out entries older than 10 seconds
    cutoff = now - timedelta(seconds=10)
    DATA[user_id] = [t for t in DATA[user_id] if t > cutoff]

    requests = len(DATA[user_id])
    delay = 0.0

    if requests > 10:
        r = requests - 10
        delay = r / 10

    return {"requests": requests, "delay": delay}