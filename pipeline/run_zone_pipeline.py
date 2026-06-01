import cv2
import numpy as np

from pathlib import Path

from detect import detect_people
from zone_engine import ZoneEngine
from zone_tracker import ZoneTracker
from debug_writer import DebugWriter
from zone_loader import load_zones

from dwell_detector import DwellDetector

from zone_event_generator import (
    create_zone_enter,
    create_zone_exit
)

from event_store import EventStore

ROOT = Path(__file__).resolve().parents[1]

VIDEO_PATH = (
    ROOT /
    "data" /
    "videos" /
    "CAM 1.mp4"
)

OUTPUT_VIDEO = (
    Path(__file__).parent /
    "debug_cam1.mp4"
)

cap = cv2.VideoCapture(
    str(VIDEO_PATH)
)

if not cap.isOpened():

    raise FileNotFoundError(
        f"Could not open video: {VIDEO_PATH}"
    )

width = int(
    cap.get(
        cv2.CAP_PROP_FRAME_WIDTH
    )
)

height = int(
    cap.get(
        cv2.CAP_PROP_FRAME_HEIGHT
    )
)

fps = cap.get(
    cv2.CAP_PROP_FPS
)

zones = load_zones(
    "CAM1",
    width,
    height
)

print("\nLoaded Zones\n")

for zone_name in zones:

    print(zone_name)

zone_engine = ZoneEngine(
    zones
)

zone_tracker = ZoneTracker()

dwell = DwellDetector(
    fps
)

event_store = EventStore()

writer = DebugWriter(
    str(OUTPUT_VIDEO),
    width,
    height,
    fps
)

frame_no = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_no += 1

    results = detect_people(
        frame
    )

    if len(results) == 0:

        writer.write(
            frame
        )

        continue

    boxes = results[0].boxes

    if boxes.id is None:

        writer.write(
            frame
        )

        continue

    ids = boxes.id.cpu().numpy()

    xyxy = (
        boxes.xyxy
        .cpu()
        .numpy()
    )

    for zone_name, polygon in zones.items():

        pts = np.array(
            polygon,
            dtype=np.int32
        )

        cv2.polylines(
            frame,
            [pts],
            True,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            zone_name,
            tuple(pts[0]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    for track_id, box in zip(
        ids,
        xyxy
    ):

        x1, y1, x2, y2 = box

        cx = int(
            (x1 + x2)
            /
            2
        )

        cy = int(y2)

        zone = zone_engine.get_zone(
            cx,
            cy
        )

        visitor_id = (
            f"VIS_{int(track_id)}"
        )

        change = (
            zone_tracker.update(
                visitor_id,
                zone
            )
        )

        if change:

            old_zone, new_zone = change

            if old_zone:

                dwell_seconds = (
                    dwell.exit(
                        visitor_id,
                        old_zone,
                        frame_no
                    )
                )

                event = (
                    create_zone_exit(
                        visitor_id,
                        old_zone,
                        "CAM1",
                        dwell_seconds
                    )
                )

                event_store.add(
                    event
                )

                print(
                    visitor_id,
                    "ZONE_EXIT",
                    old_zone,
                    dwell_seconds
                )

            if new_zone:

                dwell.enter(
                    visitor_id,
                    new_zone,
                    frame_no
                )

                event = (
                    create_zone_enter(
                        visitor_id,
                        new_zone,
                        "CAM1"
                    )
                )

                event_store.add(
                    event
                )

                print(
                    visitor_id,
                    "ZONE_ENTER",
                    new_zone
                )

        cv2.rectangle(
            frame,
            (
                int(x1),
                int(y1)
            ),
            (
                int(x2),
                int(y2)
            ),
            (255,0,0),
            2
        )

        cv2.circle(
            frame,
            (cx,cy),
            5,
            (0,0,255),
            -1
        )

        cv2.putText(
            frame,
            visitor_id,
            (
                int(x1),
                int(y1)-10
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,0,0),
            2
        )

        if zone:

            cv2.putText(
                frame,
                zone,
                (cx,cy),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2
            )

    writer.write(
        frame
    )

cap.release()

writer.close()

event_store.save()

print(
    "\nDebug video saved:",
    OUTPUT_VIDEO
)

print(
    "\nEvents saved to zone_events.json"
)