from unittest import TestCase
from app.services.polygon_external_api import PolygonExternalApi
from datetime import date
from time import sleep
import os


class PolygonExternalApiTest(TestCase):

    def test_get_stock_daily_price(self):
        polygon_external_api = PolygonExternalApi()
        stocks_checked = {"AAPL": 130.15, "GOOGL": 88.02, "AMZN": 87.36}	
        for stock_name, real_value in stocks_checked.items():
            if os.environ.get('POLYGON_API_KEY') is not None:
                price = polygon_external_api.get_stock_daily_price(stock_name, date(year=2023, month=1, day=9))
                self.assertIsInstance(price, float)
                self.assertGreater(price, 0)
                self.assertEqual(price, real_value)
                sleep(1)
            else:
                print("To run the test 'test_get_stock_daily_price' you need to set the environment variable 'POLYGON_API_KEY'")
            
