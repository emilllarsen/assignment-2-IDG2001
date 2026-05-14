"""Country data endpoint."""
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.olympic_event import OlympicEvent
from app.utils.response_format import format_response
from app.utils.token_dep import consume_token, deduct_token
from app.utils.cache import get_cached, store_cache

router = APIRouter()


@router.get("/country/{noc}")
def get_country(
    noc: str,
    request: Request,
    fmt: str = Query(default="json"),
    db: Session = Depends(get_db),
    user=Depends(consume_token),
):
    """Return medal summary for a country grouped by sport.

    First checks the cache. If the data is already stored, we return it immediately without touching the database.
    If not found in the cache, we query the database and then store the result
    in the cache for next time.
    """
    cache_key = f"{request.url.path}?{request.url.query}"

    cached_data = get_cached(cache_key)
    if cached_data is not None:
        # We got a hit! Return the stored data without querying the database.
        deduct_token(user, db)
        return format_response(cached_data, fmt)

    noc = noc.upper()
    matching_records = db.query(OlympicEvent).filter(OlympicEvent.noc == noc).all()

    if not matching_records:
        raise HTTPException(status_code=404, detail="Country not found")

    deduct_token(user, db)

    sports = {}
    for row in rows:
        sport = row.sport
        if sport not in sports:
            sports[sport] = {"gold": 0, "silver": 0, "bronze": 0, "participations": 0}
        sports[sport]["participations"] += 1
        if row.medal == "Gold":
            sports[sport]["gold"] += 1
        elif row.medal == "Silver":
            sports[sport]["silver"] += 1
        elif row.medal == "Bronze":
            sports[sport]["bronze"] += 1

    data = {"noc": noc, "sports": sports}

    store_cache(cache_key, data)

    return format_response(data, fmt)
