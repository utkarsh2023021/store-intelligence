from pathlib import Path

from ultralytics import YOLO

MODEL_PATH = Path(__file__).resolve().parent / "yolov8n.pt"

model = YOLO(str(MODEL_PATH))

def detect_people(frame):

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=[0],
        conf=0.35,
        verbose=False
    )

    return results
