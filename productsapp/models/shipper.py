from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Integer,
    ForeignKey,
    DECIMAL
)

class Shipper(Base):
    id = Column(BigInteger, primary_key=True, nullable=False)
    company_name = Column(String(length=126), nullable=False)
    phone = Column(Integer, nullable=False)
