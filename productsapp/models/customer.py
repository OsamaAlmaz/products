from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime

)
from sqlalchemy import relationship
from base import BaseModel
from base import Base

class Customer(BaseModel):
    __tablename__ = 'customer'
    id = Column(BigInteger, primary_key= True)
    first_name = Column(String(length=126), nullable=True)
    last_name = Column(String(length=126),nullable=True)
    phone = Column(Integer,nullable=True)
    email = Column(String(length=126), nullable=True)
    timestamp = Column (DateTime())
