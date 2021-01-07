
from productsapp.main import Engine
from flask_restful import Resource
from productsapp.context import MainContext
from sqlalchemy.orm import Session


engine = Engine()
session = engine.session_maker()

class MainResource (Resource):
    def __init__(self):
        self.context = MainContext(session)
    



