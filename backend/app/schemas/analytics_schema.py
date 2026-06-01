from pydantic import BaseModel
from typing import Dict


class ZoneAnalyticsResponse(
    BaseModel
):

    data: Dict[str, float]