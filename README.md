# Fintual code homework

## Introduction

## Portfolio Class
### Descripción

This class implements a simple investment portfolio, designed to calculate the return between two given dates. Each portfolio contains a collection of StockAccounts, and each stock account has a method to get its price on a given date.

 ### functions
Constructor: Initializes a new portfolio with a collection of stock accounts.
Profit Method:
Receives two dates as input.
Calculates the total return of the portfolio between those two dates. Also returns the annualized % in case the boolean parameter annualized is True

## StockAccount Class

### Description
This class represents a stock account, where there is 1 stock object and the number of shares of that object
### functions
This class has a function called value that returns the product between the share price of a given date and the number of shares.

## Stock Class
### Description
This class represents a stock and has a name as attributes and a price method.
A new parameter called data_interface was added that allows the stock price to be queried given its name and a date, using external information.

# Installation

## Clonar el repositorio
git clone https://github.com/mperalta92/fintual-homework.git

## Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate
```
## Installing dependencies
```bash
pip install -r requirements.txt

```
## make .env file
implemented the price method of a stock with an API service called Polygon.io
When you create an account, they give you a free API_KEY and you can put it in a .env file to check prices in real time. Anyway, I have an API_KEY that you can use when reviewing this assignment. Just send me an email and I will send the API_KEY to do the tests. Otherwise, the Tests of the PolygonExternalAPITest class will fail.

To create the .env file you can copy the .env-example file add the API_KEY and rename the file to .env


### Run testing
```bash
python -m unittest discover tests -p '*_test.py'
```

# Contributions:

Contributions are welcome! If you find any bugs or want to add new features, please create an issue or pull request.

# Author

Ricardo Matías Peralta Muñoz
mperalta92@gmail.com
