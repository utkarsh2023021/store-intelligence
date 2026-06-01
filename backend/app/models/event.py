from sqlalchemy import Column,String,DateTime,Float,Boolean,JSON
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(String,primary_key=True,index=True)

    store_id = Column(String,index=True)

    visitor_id = Column(String,index=True)

    event_type = Column(String,index=True)

    timestamp = Column(DateTime)

    zone_id = Column(String)

    camera_id = Column(String)

    confidence = Column(Float)

    is_staff = Column(Boolean,default=False)

    metadata_ = Column("metadata", JSON)