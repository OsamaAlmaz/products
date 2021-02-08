from productsapp.manager.base import AbstractManager
from sqlalchemy.orm import Session
import datetime
from productsapp.models.main import Products
from productsapp.main import Engine
from productsapp.manager.base import AbstractManager
from productsapp.data_access.products import ProductsAccess

engine = Engine()
session = engine.session_maker()


# need to implement the data_access module.
class ProductsManager(AbstractManager):
    _access = ProductsAccess
    def __init__ (self, session: Session):
        self._session = session
        self._access = ProductsAccess(session)
        
    def create(
        self,
        title: str,
        price:int, 
        brand_name:str, 
        description: str, 
        specifications: str, 
        model_number: int, 
        image_url: str, 
        ts) -> Products:
        obj = self._access.get_title(title)
        if not obj:
            return
        return self._access.create(
            title, 
            price, 
            brand_name, 
            description, 
            specifications, 
            model_number,
            image_url, 
            ts
        )

    def get_session(self):
        return self._session
    

    def get_id(self, id:int):
        products_obj = self._access.get(id)
        return products_obj
    def get_list_count(self):
        return self._access.get_list_count()
    
    def get_name(self, name: str):
        return self._access.get_name(name)
    
    def update(self, id: int, product: Products) -> Products:
        product_data = self._access.update(
            Products.id,
            Products.price, 
            Products.brand_name,
            Products.description,
            Products.specifications,
            Products.model_number,
            Products.image_url,
            Products.ts
            )
        return product_data

    
    def remove(self, id: int):
        result = self.get_id(id)
        if result:
            self._access.remove(id)
    
    def list(self):
        return self._access.list()