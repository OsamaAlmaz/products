from flask_restful import Resource
from flask_security import login_required, roles_accepted
from productsapp.models.main import Website
from typing import List, Tuple
from productsapp.service.core import MainResource
from sqlalchemy.orm import Session
from productsapp.models.main import Website
import json 
from productsapp.client.website import WebsiteSchema


class WebsiteResource (MainResource):
    def __init__ (self):
        super().__init__()
    
    schema = WebsiteSchema()
        
    def read(self, skip: int, limit: int) -> Tuple[int, List[Website]]: 
        return self.context.website_manager.list()
        
    def read_one (self, id: int):
        return self.context.website_manager.get(id) or None
    def create_one(self, website: Website):
        return self.context.website_manager.create(
            website.website_name, 
            website.website_base_url
        )
    
    @roles_accepted('admin')
    def create(self, website: Website):
        return self.context.website_manager.create(
            website.website_name, 
            website.website_base_url
        )

    @roles_accepted('admin')
    def update (self, id: int, website: Website) -> Website:
        return 