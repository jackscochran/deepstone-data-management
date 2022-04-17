

def process_training_set_1(ticker):

    training_data = {}

    financials = database.get_historical_financials(ticker)

    for financial in financials:
        date = financial.date + 45
        training_data[date] = []


        math_helper.divide((data_sources['key_metrics'][i]['peRatio'] - data_sources['key_metrics'][i+1]['peRatio']), data_sources['key_metrics'][i+1]['peRatio']),
        data_sources['balance_sheets'][i]['growthTotalAssets'],
        data_sources['balance_sheets'][i]['growthTotalCurrentAssets'],
        data_sources['balance_sheets'][i]['growthTotalLiabilities'],
        data_sources['balance_sheets'][i]['growthTotalCurrentLiabilities'],
        data_sources['balance_sheets'][i]['growthTotalAssets'] - data_sources['balance_sheets'][i]['growthTotalLiabilities'],
        data_sources['income_statements'][i]['growthRevenue'],
        data_sources['income_statements'][i]['growthNetIncome'],
        data_sources['cashflow_statements'][i]['growthNetCashProvidedByOperatingActivites'],
        data_sources['cashflow_statements'][i]['growthNetCashUsedForInvestingActivites'],
        data_sources['cashflow_statements'][i]['growthNetCashUsedProvidedByFinancingActivities'],
        data_sources['balance_sheets'][i]['growthCashAndCashEquivalents'],
        math_helper.divide((data_sources['key_metrics'][i]['capexPerShare'] - data_sources['key_metrics'][i+1]['capexPerShare']), data_sources['key_metrics'][i+1]['capexPerShare']),
        math_helper.divide((data_sources['key_metrics'][i]['pbRatio'] - data_sources['key_metrics'][i+1]['pbRatio']), data_sources['key_metrics'][i+1]['pbRatio']),
        math_helper.divide((data_sources['key_metrics'][i]['cashPerShare'] - data_sources['key_metrics'][i+1]['cashPerShare']), data_sources['key_metrics'][i+1]['cashPerShare']),
        math_helper.divide((data_sources['key_metrics'][i]['currentRatio'] - data_sources['key_metrics'][i+1]['currentRatio']), data_sources['key_metrics'][i+1]['currentRatio']),
        data_sources['income_statements'][i]['growthGrossProfitRatio'],
        math_helper.divide((data_sources['key_metrics'][i]['returnOnTangibleAssets'] - data_sources['key_metrics'][i+1]['returnOnTangibleAssets']), data_sources['key_metrics'][i+1]['returnOnTangibleAssets']),
        data_sources['income_statements'][i]['growthEPS'],

    return #{date: [2,3,2,5,...]}


TRAINING_SETS = [
    {
        'labels': [
            'pe',
            'assets',
            'current_assets',
            'liabilities',
            'current_liabilities',
            'book_value',
            'revenue',
            'earnings',
            'cash_from_op',
            'cash_from_inv',
            'cash_from_fin',
            'cash',
            'capex_per_share',
            'pb',
            'cash_per_share',
            'current_ratio',
            'net_margin',
            'roa',
            'eps',
            'previous_target'
            ],
        'period': 0,
        'description': '',
        'values': process_training_set_1,
        'sources': get_all_tickers
    }
]


# -------------------------------------------------------------------------


def process_target_set_1(ticker, date):

    return

TARGET_SETS = [
    {
        'type': '',
        'period': 0,
        'description': '',
        'value': process_target_set_1
    }
]