from unittest import TestCase, mock
from app.domain.stock_account import StockAccount

class StockAccountTest(TestCase):

    def test_price(self):
        name = 'AAPL'
        quantity = 10
        date = '2023-01-09'
        stock = mock.Mock()
        stock.price.return_value = 87.36
        stock_account = StockAccount(stock, quantity)
        self.assertEqual(stock_account.value(date), 873.6)