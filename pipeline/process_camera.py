import cv2

from detect import detect_people
from zone_engine import ZoneEngine
from zone_tracker import ZoneTracker
from zone_loader import load_zones

from progress_manager import (
    update_progress
)

from dwell_detector import (
    DwellDetector
)

from zone_event_generator import (
    create_zone_enter,
    create_zone_exit
)


def process_camera(
    camera_id,
    video_path,
    event_store
):

    cap = cv2.VideoCapture(
        str(video_path)
    )

    if not cap.isOpened():

        print(
            f"Could not open {video_path}"
        )

        return

    frame_count = int(
        cap.get(
            cv2.CAP_PROP_FRAME_COUNT
        )
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
        camera_id,
        width,
        height
    )

    zone_engine = ZoneEngine(
        zones
    )

    zone_tracker = ZoneTracker()

    dwell = DwellDetector(
        fps
    )

    frame_no = 0

    update_progress(
        camera_id,
        0,
        "starting"
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_no += 1

        if frame_no % 50 == 0:

            progress = int(
                (
                    frame_no
                    /
                    frame_count
                ) * 100
            )

            update_progress(
                camera_id,
                progress,
                "processing"
            )

        results = detect_people(
            frame
        )

        if len(results) == 0:
            continue

        boxes = results[0].boxes

        if boxes.id is None:
            continue

        ids = (
            boxes.id
            .cpu()
            .numpy()
        )

        xyxy = (
            boxes.xyxy
            .cpu()
            .numpy()
        )

        for track_id, box in zip(
            ids,
            xyxy
        ):

            x1, y1, x2, y2 = box

            cx = int(
                (x1 + x2)
                / 2
            )

            cy = int(y2)

            zone = (
                zone_engine.get_zone(
                    cx,
                    cy
                )
            )

            visitor_id = (
                f"{camera_id}_VIS_{int(track_id)}"
            )

            change = (
                zone_tracker.update(
                    visitor_id,
                    zone
                )
            )

            if not change:
                continue

            old_zone, new_zone = change

            if old_zone:

                dwell_seconds = (
                    dwell.exit(
                        visitor_id,
                        old_zone,
                        frame_no
                    )
                )

                event_store.add(

                    create_zone_exit(
                        visitor_id,
                        old_zone,
                        camera_id,
                        dwell_seconds
                    )
                )

            if new_zone:

                dwell.enter(
                    visitor_id,
                    new_zone,
                    frame_no
                )

                event_store.add(

                    create_zone_enter(
                        visitor_id,
                        new_zone,
                        camera_id
                    )
                )

    update_progress(
        camera_id,
        100,
        "completed"
    )

    cap.release()