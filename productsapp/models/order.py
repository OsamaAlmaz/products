from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Integer,
    ForeignKey,
    DECIMAL,
    UniqueConstraint,
    Index
)
from models.base import BaseModel
from sqlalchemy.schema import ForeignKeyConstraint
from sqlalchemy.orm import relationship
from models.products import Products

class Order(BaseModel):
    __tablename__ = 'order'
    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, 
                         ForeignKey("customer.id", ondelete="CASCADE"),
                         nullable=False)
    product_id = Column(BigInteger,
                        ForeignKey("products.id"), ondelete="CASCADE",
                        nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
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
        UniqueConstraint("customer_id","product_id"),
        Index("customer_id_index", "customer_id")
    )
