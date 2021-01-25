from marshmallow import validate, Schema, post_load, fields
from productsapp.models.main import Website

class WebsiteSchema (Schema):
    __model__ = Website
    _endpoint = '/website'

    class Meta:
        type_ = "website"
    
    id = fields.String()
    website_name = fields.String(dumpy_only=True)
    website_base_url = fields.String(dumpy_only=True)

    
    @post_load
    def make_object(self, data):
        return self.__model__(**data)
    
