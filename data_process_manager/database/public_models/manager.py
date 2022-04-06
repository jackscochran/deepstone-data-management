import mongoengine
import pytest

from . import company
from . import market_price
from . import financials

def connect_test_db():
    return mongoengine.connect(db='testPublicDB', alias='publicDB', host='localhost:27017')

def delete_test_db():
    db = connect_test_db()
    db.drop_database('testPublicDB')

def connect_production_db():
    return mongoengine.connect(db='publicDB', alias='publicDB', host='localhost:27017')
    
def disconnect_db():
    mongoengine.disconnect(alias='publicDB')

@pytest.fixture
def create_test_db():
    db = connect_test_db()
    yield db
    delete_test_db()

def load_database(tickers=None):
    company.load_data(tickers)
    collections = [market_price, financials]
    for collection in collections:
        collection.load_data()

def update_database(date):
    collections = [market_price, financials]
    for collection in collections:
        collection.update_data(date)
