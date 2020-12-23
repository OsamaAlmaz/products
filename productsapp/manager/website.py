from productsapp.manager.base import AbstractManager
from sqlalchemy.orm import Session
import datetime
from productsapp.models.main import Website
from productsapp.main import Engine
from productsapp.manager.base import AbstractManager
from productsapp.data_access.website import WebsiteAccess

engine = Engine()
session = engine.session_maker()

# need to implement the data_access module.
class WebsiteManager(AbstractManager):
    _access = WebsiteAccess
    def __init__ (self, session: Session):
        self._session = session
        self._access = WebsiteAccess(session)
    
    def create(self, website_name: str, website_base_url: str) -> Website:
        # see if you are trying to do any checking here.
        return self._access.create(website_name, website_base_url)

    def get_session(self):
        return self._session

        
    def get(self, id:int):
        website_obj = self._access.get(id)
        return web_obj
    
    def update_name(self, id: int, name, base_url):
        result = self.get(id)
        if result:
            self._access.update_name(id, name)
        return result
    
    def update_base_url (self, id: int, base_url: str):
        result = self.get(id)
        if result:
            self._access.update_base_url(id, base_url)
        return
