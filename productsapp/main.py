
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  productsapp.constants import constant



class Engine:
    def __init__(self):
        self._engine = create_engine(constant.sqlalchemy['url'])
       
    def get_engine(self):
        return self._engine

    def session_maker(self):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        return session

