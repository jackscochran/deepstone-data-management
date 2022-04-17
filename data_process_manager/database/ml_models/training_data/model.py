import mongoengine


class TrainingSet(mongoengine.Document):

    identifier = mongoengine.IntField(required=True, unique=True)
    featureLabels = mongoengine.ListField(required=True)
    description = mongoengine.StringField()

    meta = {
        'db_alias': 'privateDB',
        'collection': 'trainingSets'
    }


class TrainingPoint(mongoengine.Document):

    trainingSetId = mongoengine.IntField(required=True)
    source = mongoengine.StringField(required=True)
    date = mongoengine.StringField(required=True)
    featureValues = mongoengine.ListField(required=True)

    meta = {
        'db_alias': 'privateDB',
        'collection': 'trainingPoints'
    }


class TargetSet(mongoengine.Document):

    identifier = mongoengine.IntField(required=True)
    type = mongoengine.StringField(required=True)
    period = mongoengine.IntField(required=True, default=0)
    description = mongoengine.StringField()

    meta = {
        'db_alias': 'privateDB',
        'collection': 'targetSets'
    }

class TargetPoint(mongoengine.Document):

    targetSetId = mongoengine.IntField(require=True)
    source = mongoengine.StringField(required=True)
    date = mongoengine.StringField(required=True)
    value = mongoengine.FloatField(required=True)

    meta = {
        'db_alias': 'privateDB',
        'collection': 'targetPoints'
    }