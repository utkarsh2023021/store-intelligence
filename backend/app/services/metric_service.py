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
            Event.event_type == "ENTRY"
        )
        .distinct()
        .count()
    )

    billing = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .distinct()
        .count()
    )

    dwell_events = (
        db.query(Event)
        .filter(
            Event.event_type == "ZONE_DWELL"
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
        conversion_rate = billing / visitors

    return {
        "visitors": visitors,
        "conversion_rate": round(conversion_rate, 3),
        "avg_dwell": round(avg_dwell, 2),
        "queue_depth": billing
    }
