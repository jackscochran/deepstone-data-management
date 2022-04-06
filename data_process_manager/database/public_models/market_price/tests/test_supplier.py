from .. import supplier
from . import TEST_TICKER
from . import TEST_PRICES

def test_historical_prices_are_not_none():
    prices = supplier.get_historical_prices(TEST_TICKER)
    assert prices is not None

def test_prices_are_accurate():
    for i in range(len(TEST_PRICES)):
        price = supplier.get_price(TEST_PRICES[i]['ticker'], TEST_PRICES[i]['date'])
        assert price == TEST_PRICES[i]['value'], f'Price {i} is not accurate'

    