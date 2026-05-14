"""Rate Limiter - Tracks request frequency per user."""
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage: {user_id: [list of datetime timestamps]}
request_log = {}


class RequestLog(BaseModel):
    """Schema for logging a request."""
    username: str


@app.post("/{user_id}")
def add_request(user_id: str, payload: RequestLog):
    """Log a new request for a user."""
    current_time = datetime.now()
    if user_id not in request_log:
        request_log[user_id] = []

    request_log[user_id].append(current_time)

    # Clean out entries older than 10 seconds
    cutoff_time = current_time - timedelta(seconds=10)
    request_log[user_id] = [
        timestamp for timestamp in request_log[user_id]
        if timestamp > cutoff_time
    ]

    return {"message": "Request logged"}


@app.get("/{user_id}")
def get_requests(user_id: str):
    """Return request count and delay for a user."""
    current_time = datetime.now()

    if user_id not in request_log:
        return {"requests": 0, "delay": 0.0}

    # Clean out entries older than 10 seconds
    cutoff_time = current_time - timedelta(seconds=10)
    request_log[user_id] = [
        timestamp for timestamp in request_log[user_id]
        if timestamp > cutoff_time
    ]

    request_count = len(request_log[user_id])
    delay = 0.0

    if request_count > 10:
        excess_requests = request_count - 10
        delay = excess_requests / 10

    return {"requests": request_count, "delay": delay}