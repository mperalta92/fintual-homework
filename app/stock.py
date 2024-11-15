from datetime import date
from services.stocks_data_interface import StocksDataInterface

class Stock:
    
    def __init__(self, name, data_interface: StocksDataInterface):
        self.name = name
        self.data_interface = data_interface

    def get_name(self):
        return self.name

    def price(self, date: date):
        # this method is not required for the exercise, but it will be mocked in the tests
        return self.data_interface.get_price(self.name, date)