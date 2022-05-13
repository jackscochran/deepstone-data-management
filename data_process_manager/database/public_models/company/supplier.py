import requests

import os

from deepstone_data_management.data_process_manager.database.public_models import company
FMP_API_KEY = os.environ['FMP_API_KEY']

def get_ticker_list(n=None):
    api_url = f'https://fmpcloud.io/api/v3/financial-statement-symbol-lists?apikey={FMP_API_KEY}'
    tickers_with_financials = requests.get(api_url).json()

    if n is not None:
        tickers_with_financials = tickers_with_financials[:n]
    
    return tickers_with_financials

def get_sp500():
    api_url = f'https://fmpcloud.io/api/v3/sp500_constituent?apikey={FMP_API_KEY}'
    companies = requests.get(api_url).json()
    return [companyJSON['symbol'] for companyJSON in companies]

def get_company_info(ticker):
    api_url = f'https://fmpcloud.io/api/v3/profile/{ticker.upper()}?apikey={FMP_API_KEY}'
    company_profile = requests.get(api_url).json()

    if len(company_profile) > 0:
        return company_profile[0]
    else:
        return None


