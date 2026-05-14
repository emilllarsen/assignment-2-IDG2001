"""Token consumption dependency for data endpoints."""
import time
import httpx
from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

RATE_LIMITER_URL = "http://rate-limiter:8002"


def consume_token(
    x_user_id: str = Header(...),
    db: Session = Depends(get_db),
):
    """Check rate limit, then check and deduct one token."""
    user = db.query(User).filter(User.id == x_user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user ID")
    if user.tokens <= 0:
        raise HTTPException(status_code=403, detail="No tokens remaining")

    httpx.post(
        f"{RATE_LIMITER_URL}/{x_user_id}",
        json={"username": user.email},
    )

    resp = httpx.get(f"{RATE_LIMITER_URL}/{x_user_id}")
    data = resp.json()

    if data["delay"] > 0:
        time.sleep(data["delay"])

    user.tokens -= 1
    db.commit()
    db.refresh(user)
    return user