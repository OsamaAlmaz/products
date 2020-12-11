from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime

)
from sqlalchemy import relationship
from base import BaseModel


class Customer(BaseModel):
    __tablename__ = 'customer'
    id = Column(BigInteger, primary_key= True)
    first_name = Column(String(length=126), nullable=True)
    last_name = Column(String(length=126),nullable=True)
    phone = Column(Integer,nullable=True)
    email = Column(String(length=126), nullable=True)
    street = Column(String(length=126), nullable=True)
    city = Column(String(length=126),nullable=True)
    state = Column (String(length=126), nullable=True)
    zip_code = Column (String(length=126),nullable=True)
    timestamp = Column (DateTime())