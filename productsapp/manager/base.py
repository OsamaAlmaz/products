

from typing import Generic, TypeVar
T = TypeVar("T")


class AbstractManager(Generic[T]):
    """
        abstract class for the Manager.
        All manager classes must inherit from 
        AbstractManager 
    """
    def list(self):
        return NotImplementedError
    def get(self) -> T:
        return NotImplementedError
    def update(self) -> T:
        return NotImplementedError
    def delete(self):
        return NotImplementedError



