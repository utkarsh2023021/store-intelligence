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

    with open(EVENT_FILE) as f:

        return json.load(f)


def get_heatmap():

    events = load_events()

    heatmap = {}

    for event in events:

        zone = event["zone_id"]

        if zone is None:
            continue

        if zone not in heatmap:

            heatmap[zone] = {
                "visits": 0,
                "total_dwell": 0
            }

        if event["event_type"] == "ZONE_ENTER":

            heatmap[zone]["visits"] += 1

        elif event["event_type"] == "ZONE_EXIT":

            dwell = (
                event
                .get("metadata", {})
                .get(
                    "dwell_seconds",
                    0
                )
            )

            heatmap[zone][
                "total_dwell"
            ] += dwell

    return heatmap