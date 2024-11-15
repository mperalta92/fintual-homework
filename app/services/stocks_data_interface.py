from abc import ABC, abstractmethod

class StocksDataInterface(ABC):

    @abstractmethod
    def get_stock_daily_price(self, stock_name, date):
        pass
