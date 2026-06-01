from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.services.metric_service import (
    calculate_metrics
)

from app.services.funnel_service import (
    build_funnel
)

from app.services.anomaly_service import (
    detect_anomalies
)

router = APIRouter(
    prefix="/stores",
    tags=["stores"]
)

@router.get("/{store_id}/metrics")
def metrics(
    store_id: str,
    db: Session = Depends(get_db)
):
    return calculate_metrics(
        db,
        store_id
    )

@router.get("/{store_id}/funnel")
def funnel(
    store_id: str,
    db: Session = Depends(get_db)
):
    return build_funnel(
        db,
        store_id
    )

@router.get("/{store_id}/anomalies")
def anomalies(
    store_id: str,
    db: Session = Depends(get_db)
):
    return detect_anomalies(
        db,
        store_id
    )