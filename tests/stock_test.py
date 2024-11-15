from unittest import TestCase, mock
from app.stock import Stock
from app.services.stocks_data_interface import StocksDataInterface


class StockTest(TestCase):

    def test_name(self):
        name = 'AAPL'
        stock = Stock(name)
        self.assertEqual(stock.get_name(), name)

    def test_price(self):
        name = 'ANZN'
        date = '2023-01-09'
        data_interface = mock.Mock(StocksDataInterface)
        data_interface.get_stock_daily_price.return_value = 87.36
        stock = Stock(name, data_interface)
        self.assertEqual(stock.price(date), 87.36)
        