from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Integer
)


class Product (Base):
    __tablename__ = 'product'
    id = Column(BigInteger, primary_key=True)
    brand_name = Column (String(length=126), nullable=True)
    title = Column(String(length=True), nullable=True)
    price = Column(Integer, nullable=True)
    ts = Column(DateTime())
    description = Column()
    contact_message = Column()
    

