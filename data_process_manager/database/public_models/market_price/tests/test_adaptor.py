from .. import adaptor
from ...manager import create_test_db
from ... import manager

from . import TEST_TICKER
from . import TEST_PRICES


def test_price_model(create_test_db):
    for i in [0,1,3,4]:
        price = TEST_PRICES[i]
        adaptor.__load_price__(price['ticker'], price['date'])
        entry = adaptor.get_price_from_db(price['ticker'], price['date'])
        assert price['ticker'] == entry.ticker and price['date'] == entry.date and price['value'] == entry.value, f'Price {i} failed to load' 


def test_get_company_is_none(create_test_db):
    price = TEST_PRICES[0]
    entry = adaptor.get_price_from_db(price['ticker'], price['date'])
    assert entry is None


def test_load_historical_prices(create_test_db):
    adaptor.__load_historical_prices__(TEST_TICKER)

    for i in range(len(TEST_PRICES)):
        price = TEST_PRICES[i]
        if price['ticker'] != TEST_TICKER or price['value'] is None:
            continue

        price_model = adaptor.get_price_from_db(price['ticker'], price['date'])

        assert price_model.value == price['value']
