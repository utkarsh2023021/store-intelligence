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


def get_top_zones():

    events = load_events()

    counts = {}

    for event in events:

        if event["event_type"] != "ZONE_ENTER":
            continue

        zone = event["zone_id"]

        counts[zone] = (
            counts.get(zone, 0)
            + 1
        )

    return counts


def get_dwell_stats():

    events = load_events()

    zone_dwell = {}

    zone_count = {}

    for event in events:

        if event["event_type"] != "ZONE_EXIT":
            continue

        zone = event["zone_id"]

        dwell = (
            event
            .get("metadata", {})
            .get("dwell_seconds", 0)
        )

        zone_dwell[zone] = (
            zone_dwell.get(zone, 0)
            + dwell
        )

        zone_count[zone] = (
            zone_count.get(zone, 0)
            + 1
        )

    result = {}

    for zone in zone_dwell:

        result[zone] = round(
            zone_dwell[zone]
            /
            zone_count[zone],
            2
        )

    return result


def get_funnel():

    events = load_events()

    visitors = {}

    for event in events:

        visitor = event["visitor_id"]

        zone = event["zone_id"]

        if visitor not in visitors:

            visitors[visitor] = set()

        visitors[visitor].add(zone)

    result = {}

    for zones in visitors.values():

        for zone in zones:

            result[zone] = (
                result.get(zone, 0)
                + 1
            )

    return result

def get_summary():

    top_zones = get_top_zones()

    dwell = get_dwell_stats()

    funnel = get_funnel()

    return {

        "total_visitors":

            len(
                set(
                    event["visitor_id"]
                    for event in load_events()
                )
            ),

        "total_events":

            len(
                load_events()
            ),

        "top_zones":
            top_zones,

        "avg_dwell":
            dwell,

        "funnel":
            funnel
    }