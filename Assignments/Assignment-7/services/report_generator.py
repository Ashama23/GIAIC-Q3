# services/report_generator.py
from abc import ABC, abstractmethod

class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class StockReport(ReportStrategy):
    def generate(self, products):
        return "\n".join(p.display_info() for p in products)

class TransactionReport(ReportStrategy):
    def generate(self, transactions):
        return "\n".join(
            f"{t.timestamp}: {t.type} {t.quantity} of {t.product.name}"
            for t in transactions
        )

class ReportGenerator:
    def __init__(self, strategy: ReportStrategy):
        self._strategy = strategy
    
    def generate_report(self, data):
        return self._strategy.generate(data)