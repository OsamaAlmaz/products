from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    Index

)
from sqlalchemy.orm import relationship
from base import BaseModel
from base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint
Base = declarative_base()
import datetime

class BaseModel(Base):
    __abstract__ = True
    created_date = Column(DateTime(), default= datetime.datetime.utcnow())
    update_date = Column(DateTime(), default=datetime.datetime.utcnow())
    delete_date = Column(DateTime())


class Website(BaseModel):
    __tablename__ = 'website'
    id = Column (BigInteger, primary_key=True)
    website_name = Column (String(length=True), nullable=False)
    website_base_url = Column(String(length=True), nullable=False)




class Crawler(BaseModel):
    __tablename__ = 'crawler'
    id = Column(BigInteger, primary_key= True)
    website_id = Column(BigInteger, ForeignKey("website.id",ondelete="CASCADE"), nullable=False)
    url = Column (String(length=True), nullable=False)

    def __eq__(self, other):
        return all(
            self.id == other.id,
            self.website_id == other.website_id,
            self.url==other.url
        )

    def __repr__(self):
        return "Crawler id={}, website_id={}, url={}".format(self.id, self.website_url, self.url)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.website_id


class Customer(BaseModel):
    __tablename__ = 'customer'
    id = Column(BigInteger, primary_key= True)
    first_name = Column(String(length=126), nullable=True)
    last_name = Column(String(length=126),nullable=True)
    phone = Column(Integer,nullable=True)
    email = Column(String(length=126), nullable=True)
    timestamp = Column (DateTime())


class Employee(BaseModel):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(length=126), nullable=False)
    firstname = Column(String(length=126), nullable=False)
    birthday = Column(DateTime(), nullable=False)
    hiredate = Column(DateTime(),nullable=False)
    phone = Column(Integer,nullable=True)
    salary = Column(Integer,nullable=False)

    
    def __repr__(self):
        return "<employee id={}, lastname={}, firstname={}, salary={}".format(self.id, self.lastname, self.firstname, self.salary)
    
class Products (BaseModel):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True)
    brand_name = Column (String(length=126), nullable=False)
    title = Column(String(length=True), nullable=False)
    brand = Column (String(length=True), nullable=False)
    price = Column(Integer, nullable=False)
    ts = Column(DateTime())
    description = Column(String(length=True), nullable=True)
    specifications = Column(String(length=True), nullable=True)


    def __repr__(self):
        return "<Product "

class Order(BaseModel):
    __tablename__ = 'order_item'
    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, 
                         ForeignKey("customer.id", ondelete="CASCADE"),
                         nullable=False)
    product_id = Column(BigInteger,
                        ForeignKey("products.id", ondelete="CASCADE" ),
                        nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    cost = Column(Integer, ForeignKey('products.price'),nullable=False)
    ForeignKeyConstraint(
        columns=["product_id"], refcolumns=["products.id"], ondelete="CASCADE"
    )
    ForeignKeyConstraint(
        columns=["customer_id"], refcolumns=["customer.id"], ondelete="CASCADE"
    )
    product = relationship("Products")
    customer = relationship("customer")
    __table_args__ = (
        UniqueConstraint("id"),
    )

    def __repr__(self):
        return "<Order id={}, customer_id={}, product_id={}, cost={}".format(self.id, self.customer_id, self.product_id, self.cost)
    