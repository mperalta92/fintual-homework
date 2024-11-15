from datetime import date
from app.stock_account import StockAccount

class Portfolio:

    def __init__(self):
        self.stocks = []

    def add_stock(self, stock_account: StockAccount):
        self.stocks.append(stock_account)

    def remove_stock(self, stock_account: StockAccount):
        self.stocks.remove(stock_account)

    def profit(self, initial_date: date, final_date: date, annualized: bool = False):
        total_value_on_initial_date = self._total_value(initial_date)
        total_value_on_final_date = self._total_value(final_date)
        if annualized:
            return self._annualized_return(total_value_on_initial_date, total_value_on_final_date, initial_date, final_date)
        return total_value_on_final_date - total_value_on_initial_date
    
    def _total_value(self, date: date):
        return sum([stock_account.price(date) for stock_account in self.stocks])
    
    def _annualized_return(self, initial_value, final_value, initial_date, final_date):
        days = (final_date - initial_date).days
        result = (final_value / initial_value) ** (365 / days) - 1
        return round(result, 2)