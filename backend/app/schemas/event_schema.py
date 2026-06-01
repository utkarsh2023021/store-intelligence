from pydantic import BaseModel
from datetime import datetime

class EventIn(BaseModel):
    event_id:str
    store_id:str
    visitor_id:str
    event_type:str
    timestamp:datetime
    zone_id:str|None=None
    camera_id:str|None=None
    confidence:float
    is_staff:bool=False

class EventBatch(BaseModel):
    events:list[EventIn]