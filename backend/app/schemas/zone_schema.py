from pydantic import BaseModel
from typing import List


class ZoneCreate(BaseModel):

    camera_id: str

    zone_name: str

    polygon: List[List[int]]

    image_width: int

    image_height: int


class ZoneResponse(BaseModel):

    id: int

    camera_id: str

    zone_name: str

    polygon: List[List[int]]

    image_width: int

    image_height: int

    class Config:
        from_attributes = True