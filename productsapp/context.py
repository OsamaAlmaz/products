from manager.crawler import CrawlerManager
from manager.website import WebsiteManager




class MainContext():
    def WebsiteManager(self, session):
        return WebsiteManager(session)
    
    def CrawlerManager(self, session): 
        return CrawlerManager
