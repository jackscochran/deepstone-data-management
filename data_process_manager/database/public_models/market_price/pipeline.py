
from . import supplier
from . import model
from . import adaptor

import math

def load_price(ticker, date):

    price = supplier.get_price(ticker, date)

    if price is not None:

        adaptor.add_price(ticker, date, price)

def load_prices(ticker):

    prices = supplier.get_historical_prices(ticker)

    if prices is not None:
        for date, price in prices.items():
            if not math.isnan(price):
                adaptor.add_price(ticker, str(date)[:10], price)
