"""Rate Limiter - Tracks request frequency per user."""
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# stores a list of request timestamps per user
request_log = {}


class RequestLog(BaseModel):
    """For logging a request."""
    username: str


@app.post("/{user_id}")
def add_request(user_id: str, payload: RequestLog):
    """Log a new request for a user."""
    current_time = datetime.now()  # exact time of the request
    if user_id not in request_log:
        request_log[user_id] = []  # if first time user, we create an empty array

    request_log[user_id].append(current_time)  # add the user to the log

    cutoff_time = current_time - timedelta(seconds=10)
    request_log[user_id] = [ 
        timestamp for timestamp in request_log[user_id]
        if timestamp > cutoff_time
    ]

    return {"message": "Request logged"}


@app.get("/{user_id}")
def get_requests(user_id: str):
    """Return how many requests this user has made in the last 10 seconds, and how long to delay them."""
    current_time = datetime.now()

    if user_id not in request_log:
        return {"requests": 0, "delay": 0.0}  # user has no history. delay is not needed

    # remove timestamps older than 10 seconds before counting
    cutoff_time = current_time - timedelta(seconds=10)
    request_log[user_id] = [
        timestamp for timestamp in request_log[user_id]
        if timestamp > cutoff_time
    ]

    request_count = len(request_log[user_id])
    delay = 0.0

    if request_count > 10:
        excess_requests = request_count - 10  # how many requests was over the limit
        delay = excess_requests / 10  # add 0.1 seconds delay per excess request

    return {"requests": request_count, "delay": delay}  # return the request count and delay
