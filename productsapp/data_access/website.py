from productsapp.data_access.base import BaseAccess
from productsapp.models.main import Website
from sqlalchemy.orm import Session


class WebsiteAccess (BaseAccess):
    __model__ = Website

    def __init__(self, session: Session):
        self._session = session
    
    def create(self, website_name: str, website_base_url: str) -> Website:
        website = self._create(website_name, website_base_url)
        self._session.add(website)
        self._session.commit()
        return website
    
    def _create(self, website_name, website_base_url ) -> Website:
        # put any restrictions to the website name. 
        date_now = datetime.datetime.utcnow()
        website = Website(
            website_name= website_name,
            website_base_url = website_base_url
        )
        return website
    
    def get_session(self):
        return self._session
    
        
    def get(self, id:int):
        web_obj= self._sesison.query(Website).filter(Website.id==id).first()
        if web_obj:
            return web_obj
        return web_obj
    
    def update_name(self, id: int, name, base_url):
        website = self.get(id) or None
        if website:
            self._sesison.query(Website).filter(Website.id==id).update({"website_name":name})
        return q
    # we can take a look at what should we return for both functions. 
    def update_base_url(self, id:int, base_url):
        website = self.get(id) or None
        if website:
            self._sesison.query(Website).filter(Website.id==id).update({"website_base_url": base_url})
        return
    