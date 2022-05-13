import mongoengine
import pytest

import os

from . import company
from . import market_price
from . import financials

DB_ACCOUNT = os.environ.get('DB_ACCOUNT')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def connect_test_db():
    return mongoengine.connect(db='testPublicDB', alias='publicDB', host='localhost:27017')

def delete_test_db():
    db = connect_test_db()
    db.drop_database('testPublicDB')

def connect_production_db():
    # return mongoengine.connect(db='publicDB', alias='publicDB', host='localhost:27017') # <-- for local connection
    return mongoengine.connect(host='mongodb+srv://' + DB_ACCOUNT + ':' + DB_PASSWORD + '@realmcluster.zudeo.mongodb.net/deepstonePublicDB?retryWrites=true&w=majority', alias='publicDB')
    
def disconnect_db():
    mongoengine.disconnect(alias='publicDB')

@pytest.fixture
def create_test_db():
    db = connect_test_db()
    yield db
    delete_test_db()

COLLECTIONS_TO_UPDATE = [financials, market_price]

def load_database(tickers=None):
    company.load_data(tickers)
    for collection in COLLECTIONS_TO_UPDATE:
        collection.load_data()

def update_database(date):
    for collection in COLLECTIONS_TO_UPDATE:
        collection.update_data(date)

def load_ticker(ticker):
    company.load_data([ticker])
    for collection in COLLECTIONS_TO_UPDATE:
        collection.load_ticker(ticker)