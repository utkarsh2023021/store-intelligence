from fastapi import APIRouter

from sqlalchemy.orm import Session

from fastapi import Depends

from app.database import get_db

from app.schemas.zone_schema import ZoneCreate

from app.controllers.zone_controller import (
    create_zone_controller,
    get_zones,
    get_zones_controller,
    delete_zone_controller,
    update_zone_controller
  
)

router = APIRouter(
    prefix="/zones",    
    tags=["Zones"]
)


@router.get("/")
def list_zones():

    return get_zones()

@router.post("/")
def create_zone_route(
    payload: ZoneCreate,
    db: Session = Depends(get_db)
):

    return create_zone_controller(
        db,
        payload
    )


@router.get("/{camera_id}")
def get_zones_route(
    camera_id: str,
    db: Session = Depends(get_db)
):

    return get_zones_controller(
        db,
        camera_id
    )


@router.delete("/{zone_id}")
def delete_zone_route(
    zone_id: int,
    db: Session = Depends(get_db)
):

    return delete_zone_controller(
        db,
        zone_id
    )

@router.put("/{zone_id}")
def update_zone_route(
    zone_id: int,
    payload: ZoneCreate,
    db: Session = Depends(get_db)
):

    return update_zone_controller(
        db,
        zone_id,
        payload
    )