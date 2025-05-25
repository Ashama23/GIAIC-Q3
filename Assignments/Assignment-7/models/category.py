# models/category.py
from models import BaseModel

class Category(BaseModel):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name
    
    def display_info(self):
        return f"Category {self.id}: {self.name}"