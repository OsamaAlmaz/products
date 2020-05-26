from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    BigInteger,
    String
)


class Product (Base):
    __tablename__ = 'product'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    url = Column(String)
