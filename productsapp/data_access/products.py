from productsapp.data_access.base import BaseAccess
from productsapp.models.main import Products
from sqlalchemy.orm import Session
from productsapp.manager.base import AbstractManager
from sqlalchemy.orm import Session
import datetime
from productsapp.main import Engine

engine = Engine()
session = engine.session_maker()

class ProductsAccess (BaseAccess):
    __model__ = Products

    def __init__(self, session: Session):
        self._session = session
    
    def create(
        self,
        title: str,
        price: int,
        brand_name: str, 
        description: str, 
        specifications: str, 
        model_number: int,
        image_url: str, 
        ts 
    ) -> Products:
        product = self._create(
            title,
            price, 
            brand_name, 
            description,
            specifications,
            model_number, 
            image_url, 
            ts
            )
        self._session.add(product)
        self._session.commit()
        return product
    
    def _create(
        self,
        title: str,
        price: int, 
        brand_name: str,
        description: str, 
        specifications: str, 
        model_number:int, 
        image_url:str, 
        ts
        ) -> Products:
        date_now = datetime.datetime.utcnow()
        product_item = Products(
            title, 
            price, 
            brand_name, 
            description, 
            specifications, 
            model_number,
            image_url, 
            ts
        )
        return product_item
    
    def get_session(self):
        return self._session
        
    def get(self, id:int):
        prod_obj= self._session.query(Products).filter(Products.id==id).first()
        if not prod_obj:
            return
        return prod_obj
    
    def update(self, id: int, product: Products):
        """
                title: str,
        price: int,
        brand_name: str, 
        description: str, 
        specifications: str, 
        model_number: int,
        image_url: str, 
        ts
        """
        self._session.query(Products).filter(Products.id==id).update({
            "title": Products.title,
            "price": Products.price,
            "brand_name": Products.brand_name,
            "description": Products.description,
            "specifications": Products.specifications,
            "model_number": Products.model_number,
            "image_url": Products.image_url,
            "ts": Products.image_url})
        self._session.commit()
        return

    def get_title (self, old_title: str):
        product = self._session.query(PRoducts).filter(Products.title == old_title).first()
        if product:
            return product
        return None

    def update_title(self, old_title: str, new_title: str):
        product = self.get_title(old_title) 
        if product:
            product =  self._sesison.query(Products).filter(
                Products.title==old_title).update({
                    "title": new_title})
            return product
        return None
    
    def remove(self, id: int):
        result = self.get(id)
        if result:
            self._session.query(Products).filter(Products.id==id).delete()
    
    def count_list (self) -> int:
        return self._session.query(Products).count()
    
    def list(self, limit: int = 20, skip: int = 0, filter=None):
        q = self._session.query(Products)
        if filter:
            self._filter_list(q, filter)
        count = q.count()
        q = q.offset(skip).limit(limit) 
        return count, q.all()
    
    def get_list_count() -> int:
        return self._session.query(Products).count()
        
    
    def _filter_list (query, filter):
        return
    
