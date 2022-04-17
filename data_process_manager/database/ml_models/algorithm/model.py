from email.errors import StartBoundaryNotFoundDefect
import mongoengine

class Algorithm(mongoengine.Document):

    algorithmName = mongoengine.StringField(required=True)
    trainingSetId = mongoengine(required=True)
    targetSetId = mongoengine.IntField(required=True)

    trainingStart = mongoengine.StringField(required=True) 
    dateTrainedTo = mongoengine.StringField(required=True) 

    model = mongoengine.BinaryField(required=True) # pickled ml model
    selectedForUpdates = mongoengine.BooleanField(required=True, default=False)

    meta = {
        'db_alias': 'privateDB',
        'collection': 'algorithms'
    }


class AlgorithmIdentity(mongoengine.Document):

    meta = {
        'db_alias': 'publicDB',
        'collection': 'algorithmIdentities'
    }