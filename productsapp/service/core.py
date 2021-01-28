
from productsapp.main import Engine
from flask_restful import Resource, reqparse
from productsapp.context import MainContext
from sqlalchemy.orm import Session
from flask_restful import (
    Resource as FlaskResource, Api as FlaskRestfulApi, reqparse
)
from flask_restful import reqparse
import json
from flask import request 
from marshmallow import ValidationError

engine = Engine()
session = engine.session_maker()

"""
Implement the following methods
def delete() -> remove the instance.
def patch()
def put ()
""" 



class MainResource (Resource):
    schema = None

    def __init__(self):
        self.context = MainContext(session)
    
    def create(self, obj):
        raise NotImplementedError("please implement the create method")

    def delete(self):
        raise NotImplementedError("please implement the delete method")

    def read_one(self):
        raise NotImplementedError("please implement the read_one method")
    
    def delete(self):
        raise NotImplementedError ("please implement the remove method")

    
    def get(self, **kwargs):
        if kwargs:
            self.read_one(**kwargs)
        print(**kwargs)
        print('this is **kawargs')
        parser = reqparse.RequestParser()
        parser.add_argument('limit')
        parser.add_argument('skip')
        args = parser.parse_args()
        skip = args['limit'] or 20
        limit = args['skip'] or 0
        count, result = self.read(skip, limit)
        serialized_data = self.serializer(result)
        return serialized_data

    def post(self):
        data = request.get_json()
        print(data)
        print("this is the data")
        try:
            object, err = self.schema.load(data)
        except ValidationError as e:
            return str(e), 400
        response = self.create_one(object)
        print(response.website_name)
        print("This is the")
        data = self.serializer(response)
        return data, 200
    
    def delete(self, **kwargs):
        self.remove(**kwargs)
        return
    def patch(self, id):
        data = request.get_json()
        try:
            object, err = self.schema.load(data)
        except ValidationError as e:
            return str(e), 400
        response = self.update(id, object)
        data= self.serializer(response)
        return data
    
    def put (self):
        return


    def serializer (self, data):
        """
        return serialized object in here of the serializer type. 
        """
        # make sure that the child has the schema variable.
        if not self.schema:
            raise NotImplementedError('please implement the schema for the following class')
        response = self.schema.dump(data, many=True).data
        return response
         


