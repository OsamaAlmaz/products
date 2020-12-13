from sqlalchemy import Column
from sqlalchemy import (
    String,
    DateTime,
    Integer,
    BigInteger,
    ForeignKey
)
from base import BaseModel


class Website(BaseModel):
    __tablename__ = 'website'
    id = Column (BigInteger, primary_key=True)
    website_name = Column (String(length=True), nullable=False)
    website_base_url = Column(String(length=True), nullable=False)