from fastapi import APIRouter

from app.controllers.dashboard_controller import (
    dashboard_summary_controller
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/summary")
def dashboard_summary():

    return dashboard_summary_controller()