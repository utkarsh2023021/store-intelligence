import json
from pathlib import Path

EVENT_FILE = (
    Path(__file__).parent
    /
    "zone_events.json"
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