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
    url = Column (String(length=True), nullable=False)

    def __eq__(self, other):
        return 

    def __repr__(self):
        return "Crawler id={}, website_id={}, url={}".format(self.id, self.website_url, self.url)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.website_id
    