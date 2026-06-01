from sqlalchemy import Column,Integer,Float,String
from app.database import Base

class DailyMetric(Base):
    __tablename__ = "daily_metrics"

    id = Column(Integer,primary_key=True,index=True)

    date = Column(String)

    visitors = Column(Integer)

    converted_visitors = Column(Integer)

    conversion_rate = Column(Float)

    avg_dwell = Column(Float)

    queue_depth = Column(Integer)