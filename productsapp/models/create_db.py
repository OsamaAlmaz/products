
from sqlalchemy import create_engine
from models.base import Base
from constants import constant
import logging
from sqlalchemy import MetaData
from sqlalchemy import *
from crawler import Base

from sqlalchemy import create_engine



def create_db ():
    engine = create_engine(constant.sqlalchemy['url'], echo="debug")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db ()
    metadata = MetaData()
    logging.info("all new tables have been created.")
    print(len(metadata.tables))
