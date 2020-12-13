from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime,
    ForeignKey

)
from sqlalchemy import relationship
from base import BaseModel
from base import Base

class Crawler(Base):
    __tablename__ = 'crawler'
    id = Column(BigInteger, primary_key= True)
    website_id = Column(String(length=True), ForeignKey("website.id"), ondelete="CASCADE")
    url = Column (String(length=True), )
