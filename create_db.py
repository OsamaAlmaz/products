from sqlalchemy import create_engine
from modules.base import Base

from constants import PRODUCTS_DB_URL

def main():
    engine = create_engine(PRODUCTS_DB_URL)
    Base.metadata.create_all(engine)


main()
print("All db is created")
