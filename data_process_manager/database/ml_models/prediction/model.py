import mongoengine

class Prediction(mongoengine.Document):

    meta = {
        'db_alias': 'publicDB',
        'collection': 'predictions'
    }