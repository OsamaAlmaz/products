from manager.base import BaseAbstract
from data_access.crawler import  Crawler
from sqlalchemy.orm import Session



class CrawlerManager(BaseAbstract):
    _access = Crawler
    #descide if you are planning to do any inheritance here. 
    def __init__ (self, session: Session):
        self._session = session
    
    # make a private create methods for creating a new Crawler for the system that we can later trigger. 
    def _create(self, website ) -> Crawler:
        
