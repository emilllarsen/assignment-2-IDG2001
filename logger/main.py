"""Logger service, saves request data to daily CSV files."""
import csv
import os
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# the folder where CSV log files are stored as a docker volume
LOG_DIR = "/logs"

# primary in-memory data structure, all log entries live here first
logs = []

# how many entries from logs have already been written to the CSV file.
# use this to avoid re-writing entries that are already on disk.
flush_index = 0

# how many days of log files to keep before deleting old ones
retention_days = 7


class LogEntry(BaseModel):
    """Data the main-api sends when a request is made."""
    username: str
    endpoint: str
    tokens: int


class RetentionUpdate(BaseModel):
    """Schema for changing the retention period."""
    n: int


def get_log_path(date: datetime) -> str:
    """Return the file path for a given date, e.g, /logs/2024-05-14.csv"""
    return os.path.join(LOG_DIR, date.strftime("%Y-%m-%d") + ".csv")


def delete_old_files():
    """Delete any CSV files older than retention_days days."""
    cutoff = datetime.now() - timedelta(days=retention_days)
    for filename in os.listdir(LOG_DIR):
        if not filename.endswith(".csv"):
            continue
        try:
            file_date = datetime.strptime(filename[:-4], "%Y-%m-%d")
            if file_date < cutoff:
                os.remove(os.path.join(LOG_DIR, filename))
        except ValueError:
            pass


def flush_to_file():
    """Write any unwritten entries from the `logs` list to today's CSV file."""
    global flush_index

    new_entries = logs[flush_index:]
    if not new_entries:
        return

    file_path = get_log_path(datetime.now())
    file_exists = os.path.exists(file_path)

    if not file_exists:
        delete_old_files()

    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["time", "username", "endpoint", "tokens"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(new_entries)

    flush_index = len(logs)


@app.post("/log")
def add_log(payload: LogEntry):
    """Add a new log entry to the in-memory list, then flush unwritten entries to disk."""
    entry = {
        "time": datetime.now().isoformat(),
        "username": payload.username,
        "endpoint": payload.endpoint,
        "tokens": payload.tokens,
    }

    logs.append(entry)  # store in the primary data structure first
    flush_to_file()  # write any entries that havent been written to disk yet

    return {"message": "Logged"}


@app.get("/log")
def get_log():
    """Return all log entries stored in memory."""
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": len(logs),
        "entries": logs,
    }


@app.get("/retention")
def get_retention():
    """Return how many days of log files we keep."""
    return {"n": retention_days}


@app.post("/retention")
def set_retention(payload: RetentionUpdate):
    """Update the retention period and immediately delete any files that are now too old."""
    global retention_days
    retention_days = payload.n
    delete_old_files()
    return {"n": retention_days}
