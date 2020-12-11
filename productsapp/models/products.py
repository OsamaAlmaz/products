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

class Product (BaseModel):
    __tablename__ = 'product'
    id = Column(BigInteger, primary_key=True)
    brand_name = Column (String(length=126), nullable=True)
    title = Column(String(length=True), nullable=True)
    price = Column(Integer, nullable=True)
    ts = Column(DateTime())
    description = Column()
    contact_message = Column()
    __table_args__ = (
        UniqueConstraint("ts"),
    )
