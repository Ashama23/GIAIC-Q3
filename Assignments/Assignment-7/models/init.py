# models/__init__.py
from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, id):
        self._id = id  # Encapsulation with protected attribute
        
    @property
    def id(self):
        return self._id
    
    @abstractmethod
    def display_info(self):
        pass