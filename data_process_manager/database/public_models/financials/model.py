import mongoengine

class Financials(mongoengine.Document):
    ticker = mongoengine.StringField(required=True)
    date = mongoengine.StringField(required=True)
    period = mongoengine.StringField(required=True)

    incomeStatement = mongoengine.DictField()
    balanceSheet = mongoengine.DictField()
    cashflowStatement = mongoengine.DictField()
    financialMetrics = mongoengine.DictField()

    meta = {
        'db_alias': 'publicDB',
        'collection': 'financials',
        'indexes': [
            {'fields': ('ticker', 'date', 'period'), 'unique': True}
        ]
    }