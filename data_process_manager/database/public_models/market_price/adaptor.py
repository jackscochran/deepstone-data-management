from . import supplier
from . import model
from .. import company

import mongoengine

def load_data():
    tickers = company.adaptor.get_all_tickers()
    begin_loading = False
    start_ticker = 'cnpay'
    for ticker in tickers:
        
        if ticker == start_ticker:
            begin_loading = True

        if begin_loading:
            __load_historical_prices__(ticker)

def update_data(date):

    time_to_update = True

    if not time_to_update:
        return

    tickers = company.get_all_tickers()
    for ticker in tickers:
        __load_price__(ticker, date)    

def get_price_from_db(ticker ,date):
    return model.MarketPrice.objects(ticker=ticker, date=date).first()

def __load_historical_prices__(ticker):
    prices = supplier.get_historical_prices(ticker)

    if prices is None:
        return

    print(f'Loading historical prices for {ticker}')

    for date, value in prices.items():
        date = str(date)[:10]
        __add_price__(ticker, date, value)

def __load_price__(ticker, date):
    value = supplier.get_price(ticker, date)
    __add_price__(ticker, date, value)

    return True

def __add_price__(ticker, date, value):

    if value is None:
        return False

    price_model = model.MarketPrice(ticker=ticker.lower(), date=date, value=value)

    try:
        price_model.save()
        return True
    except mongoengine.errors.NotUniqueError:
        return False