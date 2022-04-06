import mongoengine

class MarketPrice(mongoengine.Document):
    ticker = mongoengine.StringField(required=True)
    date = mongoengine.StringField(required=True)
    value = mongoengine.FloatField(required=True)

    meta = {
        'db_alias': 'publicDB',
        'collection': 'marketPrices',
        'indexes': [
            {'fields':  ('ticker', 'date'), 'unique': True}
        ]
    }