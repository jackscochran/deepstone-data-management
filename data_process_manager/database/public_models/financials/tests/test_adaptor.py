from ...manager import create_test_db
from .. import adaptor
from . import TEST_TICKER
from . import TEST_DATE
from . import TEST_PERIOD
from . import TEST_FINANCIALS

def test_financials_model(create_test_db):
    adaptor.__load_financials__(TEST_TICKER, TEST_DATE, TEST_PERIOD)

    entry = adaptor.get_financials(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    assert entry.ticker==TEST_TICKER and entry.date==TEST_DATE and entry.period==TEST_PERIOD and entry.balanceSheet is not None and entry.incomeStatement is not None and entry.cashflowStatement

def test_load_historical_financials(create_test_db):
    adaptor.__load_historical_financials__(TEST_TICKER)
    annual_entry = adaptor.get_financials(TEST_TICKER, TEST_DATE, 'annual')
    quarterly_entry = adaptor.get_financials(TEST_TICKER, TEST_DATE, 'quarter')

    assert annual_entry is not None and quarterly_entry is not None

def test_get_financials_is_none(create_test_db):
    financials = adaptor.get_financials(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    assert financials is None

def test_load_financials_of_empty_ticker_is_none(create_test_db):
    adaptor.__load_financials__('', TEST_DATE, TEST_PERIOD)
    financials = adaptor.get_financials('', TEST_DATE, TEST_PERIOD)
    assert financials is None