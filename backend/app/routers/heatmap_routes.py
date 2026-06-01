from fastapi import APIRouter

from app.controllers.heatmap_controller import (
    heatmap_controller
)

router = APIRouter(
    prefix="/heatmap",
    tags=["Heatmap"]
)


@router.get("/")
def get_heatmap_route():

    return heatmap_controller()