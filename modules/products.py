from modules.base import Base
from sqlalchemy import Column


class Product(Base):
    __tablename__ = 'product'
    id = Column()


