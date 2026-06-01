from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.event_schema import EventBatch

from app.services.ingest_service import ingest_events

router = APIRouter(
    prefix="/events",
    tags=["events"]
)

@router.post("/ingest")
def ingest(
    payload: EventBatch,
    db: Session = Depends(get_db)
):
    return ingest_events(
        db,
        payload.events
    )