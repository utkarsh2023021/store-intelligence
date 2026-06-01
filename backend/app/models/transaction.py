from sqlalchemy import Column,Integer,String,Float,DateTime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer,primary_key=True,index=True)

    invoice_number = Column(String)

    order_datetime = Column(DateTime)

    amount = Column(Float)

    salesperson = Column(String)