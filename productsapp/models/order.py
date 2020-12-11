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
from base import BaseModel

class Order(BaseModel):
    order_id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, 
                         ForeignKey("customer.id", ondelete="CASCADE"),
                         nullable=False)
    product_id = Column(BigInteger,
                        ForeignKey("products.id"), ondelete="CASCADE",
                        nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    discount = Column(DECIMAL, nullable=False)
    total = Column(Integer, nullable=False)
    shipping_date = Column(DateTime(), nullable=False)
    __table_args__ = (
        UniqueConstraint("customer_id"),
        Index("customer_id_index", "customer_id", "product_id")
    )
