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
from productsapp.models.base import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()
import datetime

class BaseModel(Base):
    __abstract__ = True
    created_date = Column(DateTime(), default=datetime.datetime.utcnow())
    update_date = Column(DateTime())
    delete_date = Column(DateTime())


class Website(BaseModel):
    __tablename__ = 'website'
    id = Column (BigInteger, primary_key=True)
    website_name = Column (String(length=225), nullable=False)
    website_base_url = Column(String(length=True), nullable=False)

"""
class Customer_Website(BaseModel):
    __tablename__ = 'customer_website'
    #add the new table here. 
"""
class Customer_Website(BaseModel):
    __tablename__ = "customer_website"
    id = Column (BigInteger, primary_key=True)
    customer_id = Column(BigInteger, 
                         ForeignKey("customer.id", ondelete="CASCADE"),
                         nullable=False)
    website_name = Column (BigInteger, 
                            ForeignKey("website.id", ondelete="CASCADE"),
                            nullable=False)
    

class Crawler(BaseModel):
    """
    the crawler is the actual job task that 
    loops through the api products provided 
    by the scheduler. it is a
    """
    __tablename__ = 'crawler'
    id = Column(BigInteger, primary_key= True)
    website_id = Column(Integer(), ForeignKey('website.id'), nullable=False, index=True)
    status = Column(String(length=True), nullable=False)
    # the value that we are searching for. it can be url, title, upc. 
    crawl_value = Column(String(length=True), nullable= False)
    # the actual type of the search, this could be a url, title, upc. 
    crawl_type = Column(String(length=True), nullable=False) # the value, might be 
    crawl_schedule = relationship("Schedule")

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

class Crawl_Status (BaseModel):
    __tablename__ = "crawl_status"
    id = Column (BigInteger, primary_key=True)
    start_date = Column(DateTime(), nullable=True, index=True)
    end_date = Column(DateTime(), nullable=True, index=True)
    crawl_info = Column(JSONB(), nullable=True)
    crawler_id = Column(BigInteger, ForeignKey('crawler.id', ondelete="CASCADE"), nullable=False)


class Schedule (BaseModel):
    """
    scheduler is the main 
    """
    __tablename__ = 'schedule'
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(length=True), nullable=False)
    customer_id = Column(BigInteger, ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
    crawl_type = Column(String(length=True), nullable=False)
    api_products_url= Column(String(length=True), nullable=False)
    


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
    title = Column(String(length=True), nullable=False)
    price = Column(Integer, nullable=False)
    brand_name = Column (String(length=126), nullable=False)
    description = Column(String(length=True), nullable=True)
    specifications = Column(String(length=True), nullable=True)
    model_number = Column(Integer, nullable=False)
    image_url = Column (String(2048))
    ts = Column(DateTime())


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
    __table_args__ = (
        UniqueConstraint("id"),
    )

    def __repr__(self):
        return "<Order id={}, customer_id={}, product_id={}, cost={}".format(self.id, self.customer_id, self.product_id, self.cost)
    