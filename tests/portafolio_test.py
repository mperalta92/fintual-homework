from unittest import TestCase, mock
from app.domain.portfolio import Portfolio
from app.domain.stock_account import StockAccount
from app.domain.stock import Stock
from datetime import date

class PortafolioTest(TestCase):

    def test_add_stocks(self):
        portfolio = Portfolio()
        first_stock = StockAccount(Stock('AAPL'), 10) 
        portfolio.add_stock(first_stock)
        self.assertEqual(portfolio.stocks, [first_stock])
        other_stock = StockAccount(Stock('GOOGL'), 25)
        portfolio.add_stock(other_stock)
        self.assertEqual(portfolio.stocks, [first_stock, other_stock])

    def test_remove_stocks(self):
        portfolio = Portfolio()
        first_stock = StockAccount(Stock('AAPL'), 10)
        portfolio.add_stock(stock_account=first_stock)
        portfolio.remove_stock(first_stock)
        self.assertEqual(portfolio.stocks, [])

    def test_profit_when_result_is_not_annualized(self):
        portfolio = Portfolio()
        stocks = [mock.Mock(Stock) for _ in range(3)]
        prices = [[100, 200], [50, 70], [100, 70]]
        for i, stock in enumerate(stocks):
            stock.price.side_effect = prices[i]
            portfolio.add_stock(StockAccount(stock, i + 1))
        initial_date = date(year=2024, month=11, day=14)
        final_date = date(year=2024, month=12, day=4)
        self.assertEqual(
            portfolio.profit(initial_date=initial_date, final_date=final_date, annualized=False),
            50
        )

    def test_profit_when_result_is_annualized(self):
        portfolio = Portfolio()
        stocks = [mock.Mock(Stock) for _ in range(3)]
        prices = [[100, 200], [50, 70], [100, 70]]
        for i, stock in enumerate(stocks):
            stock.price.side_effect = prices[i]
            portfolio.add_stock(StockAccount(stock, 1))

        initial_date = date(year=2024, month=11, day=14)
        final_date = date(year=2024, month=12, day=4)
        self.assertEqual(
            portfolio.profit(initial_date=initial_date, final_date=final_date, annualized=True),
            272.58
        )