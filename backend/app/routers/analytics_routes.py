from fastapi import APIRouter

from app.controllers.analytics_controller import (
    top_zones_controller,
    dwell_controller,
    funnel_controller
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/top-zones")
def top_zones():

    return top_zones_controller()


@router.get("/dwell")
def dwell():

    return dwell_controller()


@router.get("/funnel")
def funnel():

    return funnel_controller()