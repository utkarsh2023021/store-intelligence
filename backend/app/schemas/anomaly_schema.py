from pydantic import BaseModel

class AnomalyResponse(BaseModel):
    type: str
    severity: str
    description: str