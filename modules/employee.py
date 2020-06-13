from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    String,
    DateTime,
    Integer
)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(length=126), nullable=False)
    firstname = Column(String(length=126), nullable=False)
    birthday = Column(DateTime(), nullable=False)
    hiredate = Column(DateTime(),nullable=False)
    phone = Column(Integer,nullable=True)
    salary = Column(Integer,nullable=False)
    