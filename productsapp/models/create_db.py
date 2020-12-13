
from sqlalchemy import create_engine
from models.base import Base
from constants import constant
import logging


def create_db ():
    engine = create_engine(constant.sqlalchemy_url['url'])
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db ()
    logging.info("all new tables have been created.")
