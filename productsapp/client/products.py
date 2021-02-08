from marshmallow import validate, Schema, post_load, fields
from productsapp.models.main import Products


class ProductsSchema (Schema):
    __model__ = Products
    _endpoint = '/products'

    class Meta:
        type_ = "products"
    
    id = fields.String()
    title = fields.String(dumpy_only=True)
    price = fields.Integer(dumpy_only=True)
    brand_name = fields.String(dumpy_only=True)
    description = fields.String(dumpy_only=True)
    specifications = fields.String(dumpy_only=True)
    model_number = fields.Integer(dumpy_only=True)
    image_url = fields.String(dumpy_only=True)
    ts = fields.DateTime()


    @post_load
    def make_object(self, data):
        return self.__model__(**data)
    
