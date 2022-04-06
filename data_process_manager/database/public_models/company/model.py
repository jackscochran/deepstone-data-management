import mongoengine

class Company(mongoengine.Document):
    ticker = mongoengine.StringField(required=True, pk=True, unique=True)
    companyName = mongoengine.StringField(required=True)
    sector = mongoengine.StringField(required=True, defualt='other')
    industry = mongoengine.StringField(required=True, default='other')
    profile = mongoengine.DictField()

    meta = {
        'db_alias': 'publicDB',
        'collection': 'companies'
    }