from .. import supplier

TEST_TICKER  = 'aapl'

TEST_INFO = {
    'companyName': 'Apple Inc.',
    'industry': 'Consumer Electronics',
    'sector': 'Technology'
}

def test_supplier_ticker_list_not_none():
    tickers = supplier.get_ticker_list()
    assert tickers is not None

def test_supplier_ticker_list_is_empty():
    tickers = supplier.get_ticker_list()
    assert len(tickers) != 0

def test_supplier_company_info_is_not_none():
    company_info = supplier.get_company_info(TEST_TICKER)
    assert company_info is not None

class TestCompanyInfoIsAccurate:

    def setup(self):
        self.company_info = supplier.get_company_info(TEST_TICKER)

    def test_company_name(self):
        assert self.company_info['companyName'] == TEST_INFO['companyName']

    def test_industry(self):
        assert self.company_info['industry'] == TEST_INFO['industry']

    def test_sector(self):
        assert self.company_info['sector'] == TEST_INFO['sector']
