from .. import database

import pytest

@pytest.mark.databaseload
class TestPublicDatabaseLoad:

    def setup(self):
        self.tickers = ['tsla', 'amzn']

    def test_db_connection(self):
        database.public_models.manager.connect_test_db()

    def test_function_call(self):
        database.public_models.manager.load_database(self.tickers)

    def test_tickers_are_loaded(self):
        tickers_in_db = database.public_models.company.get_all_tickers()
        assert tickers_in_db == self.tickers

    def test_historical_financials_are_not_none(self):
        for ticker in self.tickers:
            company_financials = database.public_models.financials.get_historical_financials(ticker)
            assert company_financials is not None

    def test_historical_prices_are_not_none(self):
        test_date = '2022-03-29'
        for ticker in self.tickers:
            price = database.public_models.market_price.get_price_from_db(ticker, test_date)
            assert price is not None

    def test_db_deletion(self):
        database.public_models.manager.delete_test_db()


@pytest.mark.databaseupdate
class TestDatabaseUpdate:

    def setup(self):
        self.tickers = ['tsla', 'amzn']
        self.test_date = '2018-10-15'
    
    def test_db_connection_and_init(self):
        database.public_models.manager.connect_test_db()
        database.public_models.company.load_data(self.tickers)

    def test_function_call(self):
        database.public_models.manager.update_database(self.test_date)

    def test_price_is_not_none(self):
        for ticker in self.tickers:
            price = database.public_models.market_price.get_price_from_db(ticker, self.test_date)
            assert price is not None

    def test_financials_are_not_none(self):
        for ticker in self.tickers:
            for period in ['annual', 'quarter']:
                financials = database.public_models.financials.get_financials(ticker, self.test_date, period)
                assert financials is not None

    def test_db_deletion(self):
        database.public_models.manager.delete_test_db()
