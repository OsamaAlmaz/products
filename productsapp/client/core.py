from marshmallow import postload 
from marshmallow_jsonapi import Schema as marshmallowJsonSchema, fields

class CoreSchema (marshmallowJsonSchema):
    __model__ = None

    # define the post_load function here. 
    # implement the id also here. 
    
