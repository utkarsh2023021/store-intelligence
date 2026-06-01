from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Zone(Base):

    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)

    camera_id = Column(String, nullable=False)

    zone_name = Column(String, nullable=False)

    polygon = Column(Text, nullable=False)

    image_width = Column(Integer)
    
    image_height = Column(Integer)