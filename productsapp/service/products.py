from flask_restful import Resource
from flask_security import login_required, roles_accepted
from typing import List, Tuple
from productsapp.service.core import MainResource
from sqlalchemy.orm import Session
from productsapp.models.main import Products
import json 
from productsapp.client.products import ProductsSchema


class ProductsResource (MainResource):
    def __init__ (self):
        super().__init__()
    
    schema = ProductsSchema()
        
    def read(self, skip: int, limit: int) -> Tuple[int, List[Products]]: 
        return self.context.products_manager.list()
        
    def read_one (self, id: int):
        return self.context.products_manager.get(id) or None

    @roles_accepted('admin')
    def create(self, products: Products):
        return self.context.products_manager.create(
            products.title,
            products.price,
            products.brand_name,
            products.description,
            products.specifications,
            products.model_number,
            products.image_url,
            products.ts
        )
    

    @roles_accepted('admin')
    def remove(self, id):
        self.context.products_manager.remove(id)
        return

    @roles_accepted('admin')
    def update (self, id:int, products: Products):
        return self.context.products_manager.update(
            products.title,
            products.price,
            products.brand_name,
            products.description,
            products.specifications,
            products.model_number,
            products.image_url,
            products.ts
            )

