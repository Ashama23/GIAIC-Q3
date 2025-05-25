# main.py
from models.product import Product
from models.category import Category
from models.transaction import Transaction
from services.inventory_manager import InventoryManager
from services.report_generator import StockReport, TransactionReport, ReportGenerator

def main():
    # Initialize inventory
    inventory = InventoryManager()
    
    # Create categories
    electronics = Category("cat1", "Electronics")
    groceries = Category("cat2", "Groceries")
    
    # Add products
    p1 = Product("prod1", "Laptop", 999.99, 10, electronics)
    p2 = Product("prod2", "Milk", 2.99, 50, groceries)
    
    inventory.add_product(p1)
    inventory.add_product(p2)
    
    # Process transactions
    t1 = Transaction(p1, 2, 'sale')
    t2 = Transaction(p2, 10, 'restock')
    
    print(inventory.process_transaction(t1))
    print(inventory.process_transaction(t2))
    
    # Generate reports
    stock_report = ReportGenerator(StockReport())
    print("\nStock Report:")
    print(stock_report.generate_report(inventory.products))
    
    transaction_report = ReportGenerator(TransactionReport())
    print("\nTransaction Report:")
    print(transaction_report.generate_report(inventory.transactions))

if __name__ == "__main__":
    main()