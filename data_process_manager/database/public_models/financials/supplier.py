import requests
import os
import math

FMP_API_KEY = os.environ['FMP_API_KEY']

def get_financial_statements(ticker, date, period):
    return __format_financials__(
        get_income_statement(ticker, date, period),
        get_balance_sheet(ticker, date, period),
        get_cashflow_statement(ticker, date, period),
        get_financial_metrics(ticker, date, period)
    )

def get_historical_financial_statements(ticker, period):

    financials = []

    statements = {
        "income_statements": get_historical_income_statements(ticker, period),
        "balance_sheets": get_historical_balance_sheets(ticker, period),
        "cashflow_statements": get_historical_cashflow_statements(ticker, period),
        "financial_metrics": get_historical_financial_metrics(ticker, period)
    }

    length_proxy = math.inf

    for statement in statements:
        if statements(statement) is not None:
            if length_proxy > len(statements[statement]):
                length_proxy =  len(statements[statement])

    if length_proxy == math.inf:
        return None

    for i in range(length_proxy):
        for statement in statements:
            financials.append(__format_financials__(
                statements[statement]['income_statements'][i],
                statements[statement]['balance_sheets'][i],
                statements[statement]['cashflow_statements'][i],
                statements[statement]['financial_metrics'][i]
            ))

    return financials

def __format_financials__(income_statement, balance_sheet, cashflow_statement, financial_metrics): 

    if income_statement is None or balance_sheet is None or cashflow_statement is None or financial_metrics is None:
        return None

    income_statement = income_statement.copy()
    balance_sheet = balance_sheet.copy()
    cashflow_statement = cashflow_statement.copy()
    financial_metrics = financial_metrics.copy()

    accounts_to_remove = ['acceptedDate', 'calendarYear', 'link', 'finalLink']
    for account in accounts_to_remove:
        income_statement.pop(account, None)
        balance_sheet.pop(account, None)
        cashflow_statement.pop(account, None)
        financial_metrics.pop(account, None)

    financials = {
        'income_statement': income_statement,
        'balance_sheet': balance_sheet,
        'cashflow_statement': cashflow_statement,
        'financial_metrics': financial_metrics
    }
        
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
