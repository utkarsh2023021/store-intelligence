from fastapi import APIRouter

from app.controllers.pipeline_controller import (
    start_pipeline,
    get_status
)

router = APIRouter(
    prefix="/pipeline",
    tags=["pipeline"]
)


@router.post("/start")
def start():

    return start_pipeline()


@router.get("/status")
def status():

    return get_status()