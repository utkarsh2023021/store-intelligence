from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base,engine

from app.models.event import Event
from app.models.transaction import Transaction
from app.models.metric import DailyMetric

from app.routers.health import router as health_router
from app.routers.events import router as event_router
from app.routers.stores import router as store_router
from app.routers.zone_routes import router as zone_router
from app.models.zone import Zone
from app.routers.analytics_routes import (
    router as analytics_router
)

from app.routers.heatmap_routes import (
    router as heatmap_router 
)

from app.routers.dashboard_routes import (
    router as dashboard_router
)

from app.routers.video_routes import (
    router as video_router 
)

from app.routers.pipeline_routes import (
    router as pipeline_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Store Intelligence API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(event_router)
app.include_router(store_router)
app.include_router(zone_router)
app.include_router(analytics_router)
app.include_router(heatmap_router)
app.include_router(dashboard_router)
app.include_router(video_router)
app.include_router(pipeline_router)
@app.get("/")
def root():
    return {
        "message":"Store Intelligence Running"
    }
