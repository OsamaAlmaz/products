from modules.base import Base
from sqlalchemy import Column
from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Integer,
    ForeignKey
)


class Order(Base):
    order_id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, 
                         ForeignKey("customer.id", ondelete="CASCADE"),
                         nullable=False)
    product
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    order_date = Column(DateTime(), nullable=False)
