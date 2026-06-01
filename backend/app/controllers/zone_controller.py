import json

from fastapi import HTTPException

from app.database import SessionLocal
from app.models.zone import Zone

from app.services.zone_service import (
    create_zone,
    get_zones_by_camera,
    delete_zone
)


def create_zone_controller(
    db,
    payload
):

    return create_zone(
        db=db,
        camera_id=payload.camera_id,
        zone_name=payload.zone_name,
        polygon=payload.polygon,
        image_width=payload.image_width,
        image_height=payload.image_height
    )


def get_zones_controller(
    db,
    camera_id
):

    zones = get_zones_by_camera(
        db,
        camera_id
    )

    result = []

    for zone in zones:

        result.append({
            "id": zone.id,
            "camera_id": zone.camera_id,
            "zone_name": zone.zone_name,
            "polygon": json.loads(
                zone.polygon
            ),
            "image_width": zone.image_width,
            "image_height": zone.image_height
        })

    return result


def delete_zone_controller(
    db,
    zone_id
):

    success = delete_zone(
        db,
        zone_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Zone not found"
        )

    return {
        "message": "deleted"
    }


def get_zones():

    db = SessionLocal()

    zones = db.query(
        Zone
    ).all()

    result = []

    for zone in zones:

        result.append({

            "id": zone.id,

            "camera_id":
                zone.camera_id,

            "zone_name":
                zone.zone_name
        })

    db.close()

    return result

def update_zone_controller(
    db,
    zone_id,
    payload
):

    zone = (
        db.query(Zone)
        .filter(
            Zone.id == zone_id
        )
        .first()
    )

    if not zone:

        raise HTTPException(
            status_code=404,
            detail="Zone not found"
        )

    zone.camera_id = (
        payload.camera_id
    )

    zone.zone_name = (
        payload.zone_name
    )

    zone.polygon = json.dumps(
        payload.polygon
    )

    zone.image_width = (
        payload.image_width
    )

    zone.image_height = (
        payload.image_height
    )

    db.commit()

    db.refresh(zone)

    return {
        "message": "updated"
    }