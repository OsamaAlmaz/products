from modules.base import Base
from sqlalchemy import (
    String,
    Column,
    BigInteger
)
from base import BaseModel

class User(BaseModel):
    __tablename__ = 'login'
    id = Column(BigInteger(), primary_key=True)
    Name = Column(String(length=126), nullable=True)
    email = Column(String(length=126), nullable=True)
    password = Column(String(length=126), nullable=True)
