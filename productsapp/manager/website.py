from productsapp.manager.base import AbstractManager
from sqlalchemy.orm import Session
import datetime
from productsapp.models.main import Website
from productsapp.main import Engine
from productsapp.manager.base import AbstractManager
engine = Engine()
session = engine.session_maker()


class WebsiteManager(AbstractManager):
    def __init__ (self, session: Session):
        self._session = session
    
    def create(self, website_name: str, website_base_url: str) -> Website:
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
        return website
    def get_session(self):
        return self._session
    
        
    def get(self, id:int):
        web_obj= self._sesison.query(Website).filter(Website.id==id).first()
        return web_obj
    
    def update_name(self, id: int, name, base_url):
        q = self._sesison.query(Website).filter(Website.id==id).update({"name":name})
        return q