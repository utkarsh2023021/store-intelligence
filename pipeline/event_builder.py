import uuid
from datetime import datetime

def build_event(
    store_id,
    visitor_id,
    event_type,
    camera_id,
    zone_id=None,
    confidence=1.0,
    metadata=None
):

    return {

        "event_id": str(uuid.uuid4()),

        "store_id": store_id,

        "visitor_id": visitor_id,

        "event_type": event_type,

        "timestamp": datetime.utcnow().isoformat(),

        "zone_id": zone_id,

        "camera_id": camera_id,

        "confidence": confidence,

        "is_staff": False,

        "metadata": metadata or {}
    }