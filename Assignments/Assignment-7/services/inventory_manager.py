# services/inventory_manager.py
class InventoryManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.products = []
            cls._instance.categories = []
            cls._instance.transactions = []
        return cls._instance
    
    def add_product(self, product):
        self.products.append(product)
    
    def find_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def process_transaction(self, transaction):
        result = transaction.process()
        self.transactions.append(transaction)
        return result