from app.services.exceptions import PolygonApiException
from app.services.stocks_data_interface import StocksDataInterface
import os
import requests

class PolygonExternalApi(StocksDataInterface):

    def __init__(self):
        self.base_url = "https://api.polygon.io"
        self.api_key = os.getenv("POLYGON_API_KEY")

    def get_stock_daily_price(self, stock_name, date):
        """
        this method requests the daily price of a stock from the Polygon API
        returns the price as a float.
        """
        url = f"{self.base_url}/v1/open-close/{stock_name}/{date.strftime('%Y-%m-%d')}?apiKey={self.api_key}"
        response = requests.get(url)
        response_json = response.json()
        if response.status_code != 200:
            error_message = response_json["message"] if 'message' in response_json else response_json["error"]
            if response.status_code in [401, 403]:
                raise PolygonApiException(PolygonApiException.ErrorType.INVALID_API_KEY, error_message)
            elif response.status_code == 404:
                raise PolygonApiException(PolygonApiException.ErrorType.NOT_FOUND, error_message)
            else:       
                raise PolygonApiException(PolygonApiException.ErrorType.UNKNOWN, error_message)
        price = response_json["close"]
        return price