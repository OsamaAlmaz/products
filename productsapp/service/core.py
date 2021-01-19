
from productsapp.main import Engine
from flask_restful import Resource, reqparse
from productsapp.context import MainContext
from sqlalchemy.orm import Session
from flask_restful import (
    Resource as FlaskResource, Api as FlaskRestfulApi, reqparse
)

engine = Engine()
session = engine.session_maker()

"""
Implement the following methods

def get() -> to get the specific instance return serialized output
def post() -> to make sure to use schema.load() to decerialize the output
def delete() -> remove the instance.
def patch()
def put ()
def serializer () 
"""



class MainResource (Resource):
    def __init__(self):
        self.context = MainContext(session)
    
    def create(self, obj):
        raise NotImplementedError("please implement the create method")

    def delete(self):
        raise NotImplementedError("please implement the delete method")

    def read_one(self):
        raise NotImplementedError("please implement the read_one method")
    
    def remove(self):
        raise NotImplementedError ("please implement the remove method")

    
    def get(self):
        # need to be implemented here
        return
    def post(self):
        return 

    def serializer (self):
        """
        return serialized object in here of the serializer type. 
        """
        return 


