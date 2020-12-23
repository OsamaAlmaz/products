from sqlalchemy.orm import Session
class BaseAccess:
    __model__ = None
    

    def __init__(self, session: Session):
        self._session = session
