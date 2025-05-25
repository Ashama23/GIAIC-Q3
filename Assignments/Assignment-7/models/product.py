# models/product.py
from models import BaseModel

class Product(BaseModel):
    def __init__(self, id, name, price, quantity, category):
        super().__init__(id)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category  # Composition
    
    def display_info(self):  # Polymorphism
        return f"{self.id}: {self.name} | ${self.price} | Qty: {self.quantity} | Category: {self.category.name}"
    
    def update_stock(self, change):
        self.quantity += change