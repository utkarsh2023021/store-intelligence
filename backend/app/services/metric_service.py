import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

EVENT_FILE = (
    ROOT /
    "pipeline" /
    "zone_events.json"
)


def load_events():
    if not EVENT_FILE.exists():
        return []

    with open(EVENT_FILE, "r") as f:
        return json.load(f)


def calculate_metrics(
    db,
    store_id: str
):
    events = load_events()
    
    # Filter events by store_id
    store_events = [
        e for e in events
        if e.get("store_id") == store_id
    ]

    # Count unique visitors (ZONE_ENTER events)
    visitors_set = set()
    for event in store_events:
        if event.get("event_type") == "ZONE_ENTER":
            visitors_set.add(event.get("visitor_id"))
    
    visitors = len(visitors_set)

    # Count exits (ZONE_EXIT events)
    exits_set = set()
    for event in store_events:
        if event.get("event_type") == "ZONE_EXIT":
            exits_set.add(event.get("visitor_id"))
    
    exits = len(exits_set)

    # Calculate average dwell time
    dwell_times = []
    for event in store_events:
        if event.get("event_type") == "ZONE_EXIT":
            dwell = (
                event
                .get("metadata", {})
                .get("dwell_seconds", 0)
            )
            dwell_times.append(dwell)

    avg_dwell = 0
    if dwell_times:
        avg_dwell = sum(dwell_times) / len(dwell_times)

    conversion_rate = 0
    if visitors:
        conversion_rate = exits / visitors

    return {
        "visitors": visitors,
        "conversion_rate": round(conversion_rate, 3),
        "avg_dwell": round(avg_dwell, 2),
        "queue_depth": exits
    }
