from pydantic import BaseModel

class MetricResponse(BaseModel):
    visitors:int
    conversion_rate:float
    avg_dwell:float
    queue_depth:int