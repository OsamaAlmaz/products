from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime

)

Base = declarative_base()

class BaseModel(Base):
    __tablename__ = 'CREATED_UPDATED_DELETED'
    created_date = Column(DateTime(), default= datetime.utcnow())
    update_date = Column(DateTime(), default=datetime.utcnow())
    delete_date = Column(DateTime())