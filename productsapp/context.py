from productsapp.manager.website import WebsiteManager



class MainContext():
    def __init__ (self, session):
        self.session = session
    
    @property
    def website_manager(self):
        return WebsiteManager(self.session)
    
