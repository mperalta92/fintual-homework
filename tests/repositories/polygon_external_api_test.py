from unittest import TestCase
from app.services.polygon_external_api import PolygonExternalApi
from datetime import date


class PolygonExternalApiTest(TestCase):

    def test_get_stock_daily_price(self):
        polygon_external_api = PolygonExternalApi()
        stock_name = "AAPL"
        price = polygon_external_api.get_stock_daily_price(stock_name, date(year=2023, month=1, day=9))
        self.assertIsInstance(price, float)
        self.assertEqual(price, 130.15)
