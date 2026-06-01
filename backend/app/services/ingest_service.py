from sqlalchemy.orm import Session
from app.models.event import Event

def ingest_events(db: Session, events):

    inserted = 0
    duplicates = 0

    for e in events:

        existing = (
            db.query(Event)
            .filter(Event.event_id == e.event_id)
            .first()
        )

        if existing:
            duplicates += 1
            continue

        event = Event(
            event_id=e.event_id,
            store_id=e.store_id,
            visitor_id=e.visitor_id,
            event_type=e.event_type,
            timestamp=e.timestamp,
            zone_id=e.zone_id,
            camera_id=e.camera_id,
            confidence=e.confidence,
            is_staff=e.is_staff,
            metadata_={}
        )

        db.add(event)
        inserted += 1

    db.commit()

    return {
        "inserted": inserted,
        "duplicates": duplicates
    }
