from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from productsapp.constants import constant
from flask import Flask


class Engine:
    def __init__(self):
        self._engine = create_engine(constant.sqlalchemy['url'])
       
    def get_engine(self):
        return self._engine

    def session_maker(self):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        return session


def create_app() -> Flask:
    flask_app = Flask(__name__)
    from productsapp.service.api_list import api_bp

    flask_app.register_blueprint(api_bp)
    return flask_app