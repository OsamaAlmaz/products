from marshmallow import validate, Schema, postload, fields
from productsapp.models.main import Website
from productsapp.client.core import Sche

class WebsiteSchema (Schema):
    __model__ = Website
    _endpoint = '/websites'

    class Meta:
        type_ = "websites"
    id = fields.String()
    website_name = fields.String()
    website_base_url = fields.String()

    #implement id in the parent class
    