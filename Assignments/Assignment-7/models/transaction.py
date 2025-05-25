# models/transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, product, quantity, transaction_type):
        self.product = product
        self.quantity = quantity
        self.type = transaction_type  # 'sale' or 'restock'
        self.timestamp = datetime.now()
    
    def process(self):
        if self.type == 'sale':
            self.product.update_stock(-self.quantity)
        else:
            self.product.update_stock(self.quantity)
        return f"Processed {self.type} of {self.quantity} {self.product.name}"