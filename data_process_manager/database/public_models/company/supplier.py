import requests
import os

API_KEY = os.environ.get('API_KEY')

def get_ticker_list(n=None):
    api_url = f'https://fmpcloud.io/api/v3/financial-statement-symbol-lists?apikey={API_KEY}'
    tickers_with_financials = requests.get(api_url).json()

    if n is not None:
        tickers_with_financials = tickers_with_financials[:n]
    
    return tickers_with_financials
    

def get_company_info(ticker):
    api_url = f'https://fmpcloud.io/api/v3/profile/{ticker.upper()}?apikey={API_KEY}'
    company_profile = requests.get(api_url).json()

    if len(company_profile) > 0:
        return company_profile[0]
    else:
        return None


