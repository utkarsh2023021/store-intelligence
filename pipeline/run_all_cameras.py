from pathlib import Path

from process_camera import (
    process_camera
)

from event_store import (
    EventStore
)

ROOT = (
    Path(__file__)
    .resolve()
    .parents[1]
)

VIDEOS = {

    "CAM1":
        ROOT /
        "data/videos/CAM 1.mp4",

    "CAM2":
        ROOT /
        "data/videos/CAM 2.mp4",

    "CAM3":
        ROOT /
        "data/videos/CAM 3.mp4",

    "CAM5":
        ROOT /
        "data/videos/CAM 5.mp4"
}

store = EventStore()

for camera_id, path in VIDEOS.items():

    print(
        f"Processing {camera_id}"
    )

    process_camera(
        camera_id,
        path,
        store
    )

store.save()

print(
    "Analytics Complete"
)
