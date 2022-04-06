from . import model
from . import supplier
from .. import company

import mongoengine


def load_data():
    tickers = company.get_all_tickers()
    for ticker in tickers:
        __load_historical_financials__(ticker)

def update_data(date):

    time_to_update = True

    if not time_to_update:
        return

    tickers = company.get_all_tickers()
    for ticker in tickers:
        for period in ['annual', 'quarter']:
            __load_financials__(ticker, date, period)

def get_historical_financials(ticker):
    historical_financials = model.Financials.objects(ticker=ticker)
    return historical_financials

def get_financials(ticker, date, period):
    financials = model.Financials.objects(ticker=ticker, period=period).order_by('-date').first()
    return financials

def __load_financials__(ticker, date, period):
    financial_statements = supplier.get_financial_statements(ticker, date, period)
    fiscal_end = financial_statements['income_statement']['date']
    __add_financials__(ticker, fiscal_end, period, financial_statements)

def __load_historical_financials__(ticker):
    for period in ['quarter', 'annual']:
        historical_financials = supplier.get_historical_financial_statements(ticker, period)
        for financials in historical_financials:
            __add_financials__(ticker, financials['income_statement']['date'], period, financials)
            
def __add_financials__(ticker, date, period, financials):
    financials_model = model.Financials(
        ticker=ticker,
        date=date,
        period=period
    )
    financials_model.incomeStatement = financials['income_statement']
    financials_model.balanceSheet = financials['balance_sheet']
    financials_model.cashflowStatement = financials['cashflow_statement']
    financials_model.financialMetrics = financials['financial_metrics']
    
    try:
        financials_model.save()
        return True
    except mongoengine.errors.NotUniqueError:
        return False

