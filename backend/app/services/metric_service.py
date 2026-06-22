from sqlalchemy.orm import Session
from app.models.event import Event

def calculate_metrics(
    db: Session,
    store_id: str
):

    visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER"
        )
        .distinct()
        .count()
    )

    exits = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_EXIT"
        )
        .distinct()
        .count()
    )

    dwell_events = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER"
        )
        .all()
    )

    avg_dwell = 0

    if dwell_events:
        avg_dwell = sum(
            (x.metadata_ or {}).get("dwell", 0)
            for x in dwell_events
        ) / len(dwell_events)

    conversion_rate = 0

    if visitors:
        conversion_rate = exits / visitors

    return {
        "visitors": visitors,
        "conversion_rate": round(conversion_rate, 3),
        "avg_dwell": round(avg_dwell, 2),
        "queue_depth": exits
    }
