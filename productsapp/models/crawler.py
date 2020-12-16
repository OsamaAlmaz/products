from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    Index

)
from sqlalchemy.orm import relationship
from base import BaseModel
from base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint


class Crawler(BaseModel):
    __tablename__ = 'crawler'
    id = Column(BigInteger, primary_key= True)
    website_id = Column(BigInteger, ForeignKey("website.id",ondelete="CASCADE"), nullable=False)
    url = Column (String(length=True), nullable=False)

    def __eq__(self, other):
        return all(
            self.id == other.id,
            self.website_id == other.website_id,
            self.url==other.url
        )

    def __repr__(self):
        return "Crawler id={}, website_id={}, url={}".format(self.id, self.website_url, self.url)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.website_id

