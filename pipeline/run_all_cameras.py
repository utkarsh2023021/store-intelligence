from pathlib import Path

from process_camera import (
    process_camera
)

from event_store import (
    EventStore
)

from progress_manager import (
    update_progress
)

ROOT = (
    Path(__file__)
    .resolve()
    .parents[1]
)

VIDEO_DIR = (
    ROOT /
    "data" /
    "videos"
)


def sort_key(path):

    stem = path.stem

    if stem.upper().startswith("CAM"):

        suffix = stem[3:]

        if suffix.isdigit():

            return (
                "CAM",
                int(suffix)
            )

    return (
        stem.upper(),
        stem
    )


videos = {

    path.stem:
        path

    for path in sorted(
        VIDEO_DIR.glob("*.mp4"),
        key=sort_key
    )
}

if not videos:

    update_progress(
        None,
        0,
        "no videos found"
    )

    print(
        "No videos found in data/videos"
    )

    raise SystemExit(0)

store = EventStore()

for camera_id, path in videos.items():

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
