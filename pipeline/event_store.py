import json
from pathlib import Path

EVENT_FILE = (
    Path(__file__).parent
    /
    "zone_events.json"
)

JSONL_OUTPUT_FILE = (
    Path(__file__).parent.parent
    /
    "data"
    /
    "output"
    /
    "events.jsonl"
)


class EventStore:

    def __init__(self):

        self.events = []

    def add(
        self,
        event
    ):

        self.events.append(
            event
        )

    def save(self):

        with open(
            EVENT_FILE,
            "w"
        ) as f:

            json.dump(
                self.events,
                f,
                indent=2
            )
        
        # Also save as JSONL format
        JSONL_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(
            JSONL_OUTPUT_FILE,
            "w"
        ) as f:
            for event in self.events:
                f.write(json.dumps(event) + "\n")