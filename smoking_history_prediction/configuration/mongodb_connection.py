from smoking_history_prediction.constants import *
from smoking_history_prediction.exception import SmokingHistoryPrediction
from urllib.parse import quote_plus
import pymongo, sys

class MongoDBClient:
    client = None
    username = quote_plus(os.getenv("username"))
    password = quote_plus(os.getenv("password"))
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                connectionURL = f"mongodb+srv://{username}:{password}@cluster0.95ipm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
                if connectionURL is None:
                    raise Exception(f"Environment key: MONGODB is not set.")
                MongoDBClient.client = pymongo.MongoClient(connectionURL)
            self.client = MongoDBClient
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise SmokingHistoryPrediction(e, sys)