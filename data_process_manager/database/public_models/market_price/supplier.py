import yahoo_fin.stock_info as yf_stock_info


def get_price(ticker, date):
    prices = get_historical_prices(ticker)
    if prices is not None:
        price = prices.get(date, None)
    else:
        price = None

    return price

def get_historical_prices(ticker):
    try:
        prices = yf_stock_info.get_data(ticker, interval='1d')['close']
    except:
        return None

    return prices.round(2)