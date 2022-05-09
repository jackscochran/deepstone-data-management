from .. import supplier

from . import TEST_TICKER
from . import TEST_DATE
from . import TEST_PERIOD
from . import TEST_FINANCIALS

def test_financials_are_accurate():
    financials = supplier.get_financial_statements(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    for statement in TEST_FINANCIALS:
        for account in TEST_FINANCIALS[statement]:
            try:
                is_equal = financials[statement][account] == TEST_FINANCIALS[statement][account]
            except KeyError as err:
                raise ValueError(f'Error in {statement}, account {account} is not in api call')

            assert is_equal, f'Account {account} in {statement} is inconsistent'


def test_format_financials():
    non_formatted_statements = {
        'balance_sheet': {
            "date" : "2018-09-29",
            "symbol" : "AAPL",
            "reportedCurrency" : "USD",
            "cik" : "0000320193",
            "fillingDate" : "2018-11-05",
            "calendarYear" : "2018",
            "period" : "FY",
            "cashAndCashEquivalents" : 25913000000,
            "shortTermInvestments" : 40388000000,
            "cashAndShortTermInvestments" : 66301000000,
            "netReceivables" : 48995000000,
            "inventory" : 3956000000,
            "otherCurrentAssets" : 12087000000,
            "totalCurrentAssets" : 131339000000,
            "propertyPlantEquipmentNet" : 41304000000,
            "goodwill" : 0.0,
            "intangibleAssets" : 0.0,
            "goodwillAndIntangibleAssets" : 0.0,
            "longTermInvestments" : 170799000000,
            "taxAssets" : 0.0,
            "otherNonCurrentAssets" : 22283000000,
            "totalNonCurrentAssets" : 234386000000,
            "otherAssets" : 0.0,
            "totalAssets" : 365725000000,
            "accountPayables" : 55888000000,
            "shortTermDebt" : 20748000000,
            "taxPayables" : 0.0,
            "deferredRevenue" : 7543000000,
            "otherCurrentLiabilities" : 32687000000,
            "totalCurrentLiabilities" : 116866000000,
            "longTermDebt" : 93735000000,
            "deferredRevenueNonCurrent" : 2797000000,
            "deferredTaxLiabilitiesNonCurrent" : 426000000,
            "otherNonCurrentLiabilities" : 44754000000,
            "totalNonCurrentLiabilities" : 141712000000,
            "otherLiabilities" : 0.0,
            "capitalLeaseObligations" : 0.0,
            "totalLiabilities" : 258578000000,
            "preferredStock" : 0.0,
            "commonStock" : 40201000000,
            "retainedEarnings" : 70400000000,
            "accumulatedOtherComprehensiveIncomeLoss" : -3454000000,
            "othertotalStockholdersEquity" : 0.0,
            "totalStockholdersEquity" : 107147000000,
            "totalLiabilitiesAndStockholdersEquity" : 365725000000,
            "minorityInterest" : 0,
            "totalEquity" : 107147000000,
            "totalLiabilitiesAndTotalEquity" : 365725000000,
            "totalInvestments" : 211187000000,
            "totalDebt" : 114483000000,
            "netDebt" : 88570000000,
            },
        'income_statement': {
            "date" : "2018-09-29",
            "symbol" : "AAPL",
            "reportedCurrency" : "USD",
            "cik" : "0000320193",
            "fillingDate" : "2018-11-05",
            "calendarYear" : "2018",
            "period" : "FY",
            "revenue" : 265595000000,
            "costOfRevenue" : 163756000000,
            "grossProfit" : 101839000000,
            "grossProfitRatio" : 0.38343718820007905,
            "researchAndDevelopmentExpenses" : 14236000000,
            "generalAndAdministrativeExpenses" : 0.0,
            "sellingAndMarketingExpenses" : 0.0,
            "sellingGeneralAndAdministrativeExpenses" : 16705000000,
            "otherExpenses" : 0.0,
            "operatingExpenses" : 30941000000,
            "costAndExpenses" : 194697000000,
            "interestIncome" : 5686000000,
            "interestExpense" : 3240000000,
            "depreciationAndAmortization" : 10903000000,
            "ebitda" : 87046000000,
            "ebitdaratio" : 0.327739603531693,
            "operatingIncome" : 70898000000,
            "operatingIncomeRatio" : 0.26694026619477024,
            "totalOtherIncomeExpensesNet" : 2005000000,
            "incomeBeforeTax" : 72903000000,
            "incomeBeforeTaxRatio" : 0.27448935409175623,
            "incomeTaxExpense" : 13372000000,
            "netIncome" : 59531000000,
            "netIncomeRatio" : 0.22414202074587247,
            "eps" : 3.0025,
            "epsdiluted" : 2.9775,
            "weightedAverageShsOut" : 19821508000,
            "weightedAverageShsOutDil" : 20000436000,
            },
        'cashflow_statement': {
            "date" : "2018-09-29",
            "symbol" : "AAPL",
            "reportedCurrency" : "USD",
            "cik" : "0000320193",
            "fillingDate" : "2018-11-05",
            "calendarYear" : "2018",
            "period" : "FY",
            "netIncome" : 59531000000,
            "depreciationAndAmortization" : 10903000000,
            "deferredIncomeTax" : -32590000000,
            "stockBasedCompensation" : 5340000000,
            "changeInWorkingCapital" : -13358000000,
            "accountsReceivables" : -5322000000,
            "inventory" : 828000000,
            "accountsPayables" : 9175000000,
            "otherWorkingCapital" : 14473000000,
            "otherNonCashItems" : 47608000000,
            "netCashProvidedByOperatingActivities" : 77434000000,
            "investmentsInPropertyPlantAndEquipment" : -13313000000,
            "acquisitionsNet" : -721000000,
            "purchasesOfInvestments" : -73227000000,
            "salesMaturitiesOfInvestments" : 104072000000,
            "otherInvestingActivites" : -745000000,
            "netCashUsedForInvestingActivites" : 16066000000,
            "debtRepayment" : -6500000000,
            "commonStockIssued" : 669000000,
            "commonStockRepurchased" : -72738000000,
            "dividendsPaid" : -13712000000,
            "otherFinancingActivites" : 4405000000,
            "netCashUsedProvidedByFinancingActivities" : -87876000000,
            "effectOfForexChangesOnCash" : 0.0,
            "netChangeInCash" : 5624000000,
            "cashAtEndOfPeriod" : 25913000000,
            "cashAtBeginningOfPeriod" : 20289000000,
            "operatingCashFlow" : 77434000000,
            "capitalExpenditure" : -13313000000,
            "freeCashFlow" : 64121000000,
            },
        'financial_metrics': {
            "symbol" : "AAPL",
            "date" : "2018-09-29",
            "period" : "FY",
            "currentRatio" : 1.1238426916297297,
            "quickRatio" : 0.9865658104153475,
            "cashRatio" : 0.22173258261598755,
            "daysOfSalesOutstanding" : 67.33249872926825,
            "daysOfInventoryOutstanding" : 8.817631109699796,
            "operatingCycle" : 76.15012983896804,
            "daysOfPayablesOutstanding" : 124.57021422115831,
            "cashConversionCycle" : -48.42008438219027,
            "grossProfitMargin" : 0.38343718820007905,
            "operatingProfitMargin" : 0.26694026619477024,
            "pretaxProfitMargin" : 0.27448935409175623,
            "netProfitMargin" : 0.22414202074587247,
            "effectiveTaxRate" : 0.18342180705869443,
            "returnOnAssets" : 0.16277530931710985,
            "returnOnEquity" : 0.5556011834209077,
            "returnOnCapitalEmployed" : 0.2848922482208801,
            "netIncomePerEBT" : 0.8165781929413056,
            "ebtPerEbit" : 1.0282800643177523,
            "ebitPerRevenue" : 0.26694026619477024,
            "debtRatio" : 0.7070285050242668,
            "debtEquityRatio" : 2.4133013523477094,
            "longTermDebtToCapitalization" : 0.46661721806831874,
            "totalDebtToCapitalization" : 0.5165501060325768,
            "interestCoverage" : 21.882098765432097,
            "cashFlowToDebtRatio" : 0.6763798991990078,
            "companyEquityMultiplier" : 3.4133013523477094,
            "receivablesTurnover" : 5.42085927135422,
            "payablesTurnover" : 2.9300744345834526,
            "inventoryTurnover" : 41.3943377148635,
            "fixedAssetTurnover" : 6.430248886306411,
            "assetTurnover" : 0.7262150522933899,
            "operatingCashFlowPerShare" : 3.9065645257666572,
            "freeCashFlowPerShare" : 3.2349203703371106,
            "cashPerShare" : 3.344901911600268,
            "payoutRatio" : 0.23033377567989788,
            "operatingCashFlowSalesRatio" : 0.29154916319960844,
            "freeCashFlowOperatingCashFlowRatio" : 0.8280729395356046,
            "cashFlowCoverageRatios" : 0.6763798991990078,
            "shortTermCoverageRatios" : 3.732118758434548,
            "capitalExpenditureCoverageRatio" : -5.816420040561857,
            "dividendPaidAndCapexCoverageRatio" : 194.0701754385965,
            "dividendPayoutRatio" : 0.23033377567989785,
            "priceBookValueRatio" : 9.81575997742828,
            "priceToBookRatio" : 9.81575997742828,
            "priceToSalesRatio" : 3.9598984706094167,
            "priceEarningsRatio" : 17.66691697269503,
            "priceToFreeCashFlowsRatio" : 16.40225876548257,
            "priceToOperatingCashFlowsRatio" : 13.582266630956788,
            "priceCashFlowRatio" : 13.582266630956788,
            "priceEarningsToGrowthRatio" : 0.5977091983097916,
            "priceSalesRatio" : 3.9598984706094167,
            "dividendYield" : 0.013037576167697424,
            "enterpriseValueMultiple" : 13.099961334254392,
            "priceFairValue" : 9.81575997742828
        }
    }
    formatted_financials = supplier.__format_financials__(
        [   
            non_formatted_statements['income_statement'],
            non_formatted_statements['balance_sheet'],
            non_formatted_statements['cashflow_statement'],
            non_formatted_statements['financial_metrics']
        ]
    )
    
    for statement in formatted_financials:
        for item in ['acceptedDate', 'calendarYear', 'link', 'finalLink']:
            assert item not in formatted_financials[statement]

def test_statement_finder_is_not_none():
    income_statements = supplier.get_historical_income_statements(TEST_TICKER, TEST_PERIOD)
    statement = supplier.__find_statement_by_date__(income_statements, TEST_DATE)
    assert statement is not None


def test_balance_sheet_is_not_None():
    balance_sheet = supplier.get_balance_sheet(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    assert balance_sheet is not None

def test_income_statement_is_not_None():
    income_statement = supplier.get_income_statement(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    assert income_statement is not None

def test_cashflow_statement_is_not_None():
    cashflow_statement = supplier.get_cashflow_statement(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    assert cashflow_statement is not None

def test_financial_metrics_is_not_None():
    financial_metrics = supplier.get_financial_metrics(TEST_TICKER, TEST_DATE, TEST_PERIOD)
    assert financial_metrics is not None


def test_historical_balance_sheets_are_not_empty():
    financials = supplier.get_historical_balance_sheets(TEST_TICKER, TEST_PERIOD)
    assert len(financials) != 0

def test_historical_income_statements_are_not_empty():
    financials = supplier.get_historical_income_statements(TEST_TICKER, TEST_PERIOD)
    assert len(financials) != 0

def test_historical_cashflow_statements_are_not_empty():
    financials = supplier.get_historical_cashflow_statements(TEST_TICKER, TEST_PERIOD)
    assert len(financials) != 0

def test_historical_financial_metrics_are_not_empty():
    financials = supplier.get_historical_financial_metrics(TEST_TICKER, TEST_PERIOD)
    assert len(financials) != 0


def test_historical_financials_dates_are_equal():
    historical_financials = supplier.get_historical_financial_statements(TEST_TICKER, TEST_PERIOD)[0]
    assert historical_financials['income_statement']['date']==historical_financials['balance_sheet']['date'] and historical_financials['income_statement']['date']==historical_financials['cashflow_statement']['date']
