from sqlalchemy.orm import Session
from app.models.event import Event

def build_funnel(
    db: Session,
    store_id: str
):

    entry = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY"
        )
        .distinct()
        .count()
    )

    zone_visit = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER"
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

    purchase = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "PURCHASE"
        )
        .distinct()
        .count()
    )

    return {
        "entry": entry,
        "zone_visit": zone_visit,
        "billing": billing,
        "purchase": purchase
    }