import cv2
import json

from pathlib import Path

from detect import detect_people
from tracker import VisitorTracker
from session_manager import SessionManager

from event_builder import build_event
from debug_video import DebugVideo


from config_loader import get_camera_config
from gate_detector import GateDetector

from event_logger import EventLogger

logger = EventLogger()

cam_config = get_camera_config("CAM3")

p1 = tuple(
    cam_config["entry_gate"]["p1"]
)

p2 = tuple(
    cam_config["entry_gate"]["p2"]
)

gate = GateDetector(
    p1,
    p2
)

ROOT_DIR = Path(__file__).resolve().parents[1]

VIDEO_PATH = ROOT_DIR / "data" / "videos" / "CAM 3.mp4"

OUTPUT_PATH = Path(__file__).resolve().parent / "events.json"

tracker = VisitorTracker()

session_manager = SessionManager()

events = []

cap = cv2.VideoCapture(str(VIDEO_PATH))

if not cap.isOpened():
    raise Exception("Video not found")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

debug = DebugVideo(
    "debug_cam3.mp4",
    width,
    height,
    fps
)

ENTRY_LINE_Y = int(height * 0.55)



while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = detect_people(frame)

    if len(results) == 0:
        continue

    boxes = results[0].boxes

    if boxes.id is None:
        continue

    ids = boxes.id.cpu().numpy()

    xyxy = boxes.xyxy.cpu().numpy()

    for track_id, box in zip(ids, xyxy):

        x1, y1, x2, y2 = box

        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        event_type = gate.update(
            int(track_id),
            cx,
            cy
        )

        cv2.line(
            frame,
            p1,
            p2,
            (255,0,255),
            4
        )

        cv2.putText(
            frame,
            f"ID:{int(track_id)}",
            (int(x1), int(y1)-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )

        if event_type:

            visitor_id = f"VIS_{int(track_id)}"

            if session_manager.should_emit(
                visitor_id,
                event_type
            ):

                events.append(
                    build_event(
                        store_id="Brigade_Bangalore",
                        visitor_id=visitor_id,
                        event_type=event_type,
                        camera_id="CAM3",
                        zone_id="ENTRY"
                    )
                )
                logger.log(event_type)

    cv2.line(
        frame,
        (0, ENTRY_LINE_Y),
        (width, ENTRY_LINE_Y),
        (0,0,255),
        3
    )

    debug.write(frame)

cap.release()
debug.close()

with open(OUTPUT_PATH, "w") as f:
    json.dump(events, f, indent=2)

print(f"events generated = {len(events)}")

print(
    logger.summary()
)