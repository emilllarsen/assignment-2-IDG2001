"""Event creation endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.olympic_event import OlympicEvent
from app.schemas import OlympicEventCreate
from app.utils.token_dep import consume_token, deduct_token

router = APIRouter()


@router.post("/event", status_code=201)
def create_event(
    payload: OlympicEventCreate,
    db: Session = Depends(get_db),
    user=Depends(consume_token),
):
    """Create a new athlete participation record."""
    event = OlympicEvent(
        name=payload.name,
        sex=payload.sex,
        age=payload.age,
        height=payload.height,
        weight=payload.weight,
        team=payload.team,
        noc=payload.noc.upper(),
        games=payload.games,
        year=payload.year,
        season=payload.season,
        city=payload.city,
        sport=payload.sport,
        event=payload.event,
        medal=payload.medal,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    deduct_token(user, db)

    return {"message": "Event created", "id": event.id}
