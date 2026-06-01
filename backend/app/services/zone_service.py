import json

from sqlalchemy.orm import Session

from app.models.zone import Zone


def create_zone(
    db: Session,
    camera_id: str,
    zone_name: str,
    polygon,
    image_width,
    image_height
):

    zone = Zone(
    camera_id=camera_id,
    zone_name=zone_name,
    polygon=json.dumps(polygon),

    image_width=image_width,
    image_height=image_height
)

    db.add(zone)

    db.commit()

    db.refresh(zone)

    return zone


def get_zones_by_camera(
    db: Session,
    camera_id: str
):

    return (
        db.query(Zone)
        .filter(
            Zone.camera_id == camera_id
        )
        .all()
    )


def delete_zone(
    db: Session,
    zone_id: int
):

    zone = (
        db.query(Zone)
        .filter(Zone.id == zone_id)
        .first()
    )

    if not zone:
        return False

    db.delete(zone)

    db.commit()

    return True