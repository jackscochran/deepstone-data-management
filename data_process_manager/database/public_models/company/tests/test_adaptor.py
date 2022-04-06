from .. import adaptor
from ...manager import create_test_db
from ... import manager

TEST_LIST = ['aapl', 'msft', 'tsla', 'amzn', 'gme']

TEST_TICKER = 'aapl'
TEST_INFO = {
    'companyName': 'Apple Inc.',
    'industry': 'Consumer Electronics',
    'sector': 'Technology'
}

def test_company_model(create_test_db):
    adaptor.__load_company__(TEST_TICKER, TEST_INFO)
    entry = adaptor.get_company(TEST_TICKER)
    assert entry.ticker == TEST_TICKER and entry.companyName == TEST_INFO['companyName'] and entry.industry == TEST_INFO['industry'] and entry.sector == TEST_INFO['sector']

def test_get_company_is_none(create_test_db):
    entry = adaptor.get_company(TEST_TICKER)
    assert entry is None

class TestCompanyAdaptor:

    def setup(self):
        manager.connect_test_db()
    
    def test_database_load(self):
        adaptor.__load_companies__(TEST_LIST)

    def test_get_all_tickers(self):
        tickers = adaptor.get_all_tickers()
        assert tickers == TEST_LIST
        
    def test_teardown(self):
        manager.delete_test_db()