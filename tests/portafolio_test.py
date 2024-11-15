from unittest import TestCase, mock
from app.portfolio import Portfolio
from app.stock import Stock
from datetime import date

class PortafolioTest(TestCase):

    def test_add_stocks(self):
        portfolio = Portfolio()
        first_stock = Stock('AAPL')
        portfolio.add_stock(first_stock)
        self.assertEqual(portfolio.stocks, [first_stock])

    def test_remove_stocks(self):
        portfolio = Portfolio()
        first_stock = Stock('AAPL')
        portfolio.add_stock(first_stock)
        portfolio.remove_stock(first_stock)
        self.assertEqual(portfolio.stocks, [])

    def test_profit_when_result_is_not_annualized(self):
        portfolio = Portfolio()
        first_stock = mock.Mock(Stock)
        second_stock = mock.Mock(Stock)
        third_stock = mock.Mock(Stock)
        first_stock.price.side_effect = [100, 200]
        second_stock.price.side_effect = [50, 70]
        third_stock.price.side_effect = [100, 70]
        portfolio.add_stock(first_stock)
        portfolio.add_stock(second_stock)
        portfolio.add_stock(third_stock)
        initial_date = date(year=2024, month=11, day=14)
        final_date = date(year=2024, month=12, day=4)
        self.assertEqual(portfolio.profit(initial_date=initial_date, final_date=final_date, annualized=False), 90)

    def test_profit_when_result_is_annualized(self):
        portfolio = Portfolio()
        first_stock = mock.Mock(Stock)
        second_stock = mock.Mock(Stock)
        third_stock = mock.Mock(Stock)
        first_stock.price.side_effect = [100, 200]
        second_stock.price.side_effect = [50, 70]
        third_stock.price.side_effect = [100, 70]
        portfolio.add_stock(first_stock)
        portfolio.add_stock(second_stock)
        portfolio.add_stock(third_stock)
        initial_date = date(year=2024, month=11, day=14)
        final_date = date(year=2024, month=12, day=4)
        #20 days between initial and final date
        # initial value = 100 + 50 + 100 = 250
        # final value = 200 + 70 + 70 = 340
        # 90 profit in 20 days
        # 90 profit in 20 days is equivalent 340/250 - 1 = 36%
        # 36% in 20 days is (1 + d%)^20 = 1.36  => d=0.36^(1/20) - 1 = 0.0154930
        # and (1 + 0.0154930)^365 = 273.5804 - 1 = 272.58
        self.assertEqual(portfolio.profit(initial_date=initial_date, final_date=final_date, annualized=True), 272.58)