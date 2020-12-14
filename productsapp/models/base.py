from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime

)
from constants import constant
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine(constant.sqlalchemy['url'])
class BaseModel(Base):
    __abstract__ = True
    created_date = Column(DateTime(), default= datetime.datetime.utcnow())
    update_date = Column(DateTime(), default=datetime.datetime.utcnow())
    delete_date = Column(DateTime())

    