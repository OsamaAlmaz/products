from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Integer,
    UniqueConstraint
)
from base import BaseModel

class Products (BaseModel):
    __tablename__ = 'product'
    id = Column(BigInteger, primary_key=True)
    brand_name = Column (String(length=126), nullable=False)
    title = Column(String(length=True), nullable=False)
    brand = Column (String(length=True), nullable=False)
    price = Column(Integer, nullable=False)
    ts = Column(DateTime())
    description = Column(String(length=True), nullable=True)
    specifications = Column(String(length=True), nullable=True)


    def __repr__(self):
        return "<Product "