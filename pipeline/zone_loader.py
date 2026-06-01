import sqlite3
import json

DB_PATH = "../backend/store.db"


def load_zones(
    camera_id,
    video_width,
    video_height
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            zone_name,
            polygon,
            image_width,
            image_height
        FROM zones
        WHERE camera_id = ?
        """,
        (camera_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    zones = {}

    for (
        zone_name,
        polygon,
        image_width,
        image_height
    ) in rows:

        polygon_points = json.loads(
            polygon
        )

        scale_x = (
            video_width /
            image_width
        )

        scale_y = (
            video_height /
            image_height
        )

        scaled_polygon = []

        for x, y in polygon_points:

            scaled_polygon.append(
                [
                    int(x * scale_x),
                    int(y * scale_y)
                ]
            )

        zones[zone_name] = scaled_polygon

    return zones