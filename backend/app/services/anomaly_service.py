from sqlalchemy.orm import Session
from app.models.event import Event

def detect_anomalies(
    db: Session,
    store_id: str
):

    anomalies = []

    billing = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .count()
    )

    if billing > 20:
        anomalies.append({
            "type": "QUEUE_SPIKE",
            "severity": "HIGH",
            "description":
            "Billing queue unusually high"
        })

    entries = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY"
        )
        .count()
    )

    purchases = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "PURCHASE"
        )
        .count()
    )

    if entries > 0:

        conversion = purchases / entries

        if conversion < 0.10:
            anomalies.append({
                "type": "CONVERSION_DROP",
                "severity": "MEDIUM",
                "description":
                "Low conversion rate detected"
            })

    return anomalies