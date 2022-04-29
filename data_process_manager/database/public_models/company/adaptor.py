from . import model
from . import supplier

import random

import mongoengine

def load_data(tickers=None):
    if tickers is None:
        tickers = random.choice(supplier.get_ticker_list(), k=3000)
    __load_companies__(tickers)


def get_all_tickers():
    companies = model.Company.objects.all()
    return [company.ticker for company in companies]

def get_company(ticker):
    company = model.Company.objects(ticker=ticker).first()
    return company


def __load_company__(ticker, company_info):

    if company_info is None:
        return


    print(f'Loading {ticker} company data into database')
    company_info = company_info.copy()

    company_model = model.Company(
        ticker = ticker.lower(),
        companyName = company_info.pop('companyName'),
        sector = company_info.pop('sector'),
        industry = company_info.pop('industry'),
        profile = company_info
    )
    try:
        company_model.save()
        return True
    except mongoengine.errors.NotUniqueError:
        return False

def __load_companies__(tickers):
    for ticker in tickers:
        company_info = supplier.get_company_info(ticker)
        __load_company__(ticker, company_info)
