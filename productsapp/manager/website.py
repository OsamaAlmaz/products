from manager.base import BaseAbstract
from data_access.crawler import  Website
from sqlalchemy.orm import Session
import datetime
from models.main import Website


"""
class Website(Base):
    __tablename__ = 'website'
    id = Column (BigInteger, primary_key=True)
    website_name = Column (String(length=True), nullable=False)
    website_base_url = Column(String(length=True), nullable=False)
"""

class WebsiteManager(BaseAbstract):
    def __init__ (self, session: Session):
        self._session = session
    
    def create(self, website_name, website_base_url) -> Website:
        website = self._create(website_name, website_base_url)
        self._session.commit(website)
        return website
    
    def _create(self, website_name, website_base_url ) -> Website:
        # put any restrictions to the website name. 
        date_now = datetime.datetime.utcnow()
        website = Website(
            website_name= website_name,
            website_base_url = website_base_url
        )
        self._session.add(website)
        self._session
        return website
        
    def get(self, id:int):
        q = self._session.query(Website).filter(Website.id=id)
        return q

    def update_name(self, id: int, name, base_url):
        
        q = self._sesison.query(Website).
        filter(Website.id=id).update({Website.name=name})
