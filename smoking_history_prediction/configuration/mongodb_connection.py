from smoking_history_prediction.constants import *
from smoking_history_prediction.exception import SmokingHistoryPrediction
from urllib.parse import quote_plus
import pymongo, sys
from smoking_history_prediction.constants import MONGODB_URL

class MongoDBClient:
    client = None
    username = quote_plus(os.getenv("username"))
    password = quote_plus(os.getenv("password"))
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                connectionURL = MONGODB_URL
                if connectionURL is None:
                    raise Exception(f"Environment key: MONGODB is not set.")
                MongoDBClient.client = pymongo.MongoClient(connectionURL)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise SmokingHistoryPrediction(e, sys)