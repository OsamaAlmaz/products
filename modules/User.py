from modules.base import Base
from sqlalchemy import (
    String,
    Column,
    BigInteger
)

class User(Base):
    __tablename__ = 'login'
    id = Column(BigInteger(), primary_key=True)
    Name = Column(String(length=126), nullable=True)
    email = Column(String(length=126), nullable=True)
    password = Column(String(length=126), nullable=True)
