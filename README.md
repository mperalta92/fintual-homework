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
git clone https://github.com/tu_usuario/portfolio_class.git

## Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate
```
## Installing dependencies
```bash
pip install -r requirements.txt

```
### Run testing
```bash
python -m unittest discover tests -p '*_test.py'
```

# Contributions:

Contributions are welcome! If you find any bugs or want to add new features, please create an issue or pull request.

# Author

Ricardo Matías Peralta Muñoz
mperalta92@gmail.com
