from app.stock import Stock


class StockAccount:
    """
    This class represent a stock account
    """

    def __init__(self, stock: Stock, quantity: int) -> None:
        self.stock = stock
        self.quantity = quantity

    def price(self, date):
        """
        this method returns the value of the stock account on a given date
        """
        return self.stock.price(date) * self.quantity
