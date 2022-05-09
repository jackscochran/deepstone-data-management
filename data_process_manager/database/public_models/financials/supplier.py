import requests
import math

import os
FMP_API_KEY = os.environ['FMP_API_KEY']

STATEMENT_NAMES = ['income_statement', 'balance_sheet', 'cashflow_statement', 'financial_metrics']

def get_financial_statements(ticker, date, period):
    return __format_financials__(
        [
            get_income_statement(ticker, date, period),
            get_balance_sheet(ticker, date, period),
            get_cashflow_statement(ticker, date, period),
            get_financial_metrics(ticker, date, period)
        ]
    )

def get_historical_financial_statements(ticker, period):

    financials = []

    statements = [
        get_historical_income_statements(ticker, period),
        get_historical_balance_sheets(ticker, period),
        get_historical_cashflow_statements(ticker, period),
        get_historical_financial_metrics(ticker, period)
    ]

    length_proxy = math.inf

    for statement in statements:
        if statement is None:
            return None
        
        if length_proxy > len(statement):
            length_proxy =  len(statement)

    if length_proxy == math.inf:
        return None # should never happen but just in case to avoid an infinite loop

    for i in range(length_proxy):
        financials.append(__format_financials__(
            [statement[i] for statement in statements]
        ))

    return financials

def __format_financials__(statements): 

    for statement in statements:
        if statement is None:
            return None

    statements = [statement.copy() for statement in statements]

    accounts_to_remove = ['acceptedDate', 'calendarYear', 'link', 'finalLink']
    for account in accounts_to_remove:
        for statement in statements:
            statement.pop(account, None)

    financials = {}

    for i in range(len(STATEMENT_NAMES)):
        financials[STATEMENT_NAMES[i]] = statements[i]
        
    return financials

def __find_statement_by_date__(statements, date):
    if statements is None:
        return None

    for statement in statements:
        if statement['date'][:7] <= date[:7]:
            return statement
    
    
def get_historical_balance_sheets(ticker, period):
    api_url = f'https://fmpcloud.io/api/v3/balance-sheet-statement/{ticker.upper()}?period={period}&apikey={FMP_API_KEY}'
    balance_sheets = requests.get(api_url).json()

    if isinstance(balance_sheets, list):
        return balance_sheets

    return None

def get_historical_income_statements(ticker, period):
    api_url = f'https://fmpcloud.io/api/v3/income-statement/{ticker.upper()}?period={period}&apikey={FMP_API_KEY}'
    income_statements = requests.get(api_url).json()

    if isinstance(income_statements, list):
        return income_statements

    return None

def get_historical_cashflow_statements(ticker, period):
    api_url = f'https://fmpcloud.io/api/v3/cash-flow-statement/{ticker.upper()}?period={period}&apikey={FMP_API_KEY}'
    cashflow_statements = requests.get(api_url).json()

    if isinstance(cashflow_statements, list):
        return cashflow_statements

    return None

def get_historical_financial_metrics(ticker, period):
    api_url = f'https://fmpcloud.io/api/v3/ratios/{ticker.upper()}?period={period}&apikey={FMP_API_KEY}'
    financial_metrics = requests.get(api_url).json()

    if isinstance(financial_metrics, list):
        return financial_metrics

    return None    


def get_balance_sheet(ticker, date, period):
    balance_sheets = get_historical_balance_sheets(ticker, period)
    return __find_statement_by_date__(balance_sheets, date)

def get_income_statement(ticker, date, period):
    income_statements = get_historical_income_statements(ticker, period)
    return __find_statement_by_date__(income_statements, date)

def get_cashflow_statement(ticker, date, period):
    cashflow_statements = get_historical_cashflow_statements(ticker, period)
    return __find_statement_by_date__(cashflow_statements, date)

def get_financial_metrics(ticker, date, period):
    financial_metrics = get_historical_financial_metrics(ticker, period)
    return __find_statement_by_date__(financial_metrics, date)
