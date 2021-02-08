from productsapp.manager.website import WebsiteManager
from productsapp.manager.products import Products


class MainContext():
    def __init__ (self, session):
        self.session = session
    
    @property
    def website_manager(self):
        return WebsiteManager(self.session)
    
    @property
    def products_manager(self):
        return ProductsManager(self.session)
    