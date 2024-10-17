from smoking_history_prediction.configuration.mongodb_connection import MongoDBClient
from smoking_history_prediction.constants import DATABASE_NAME
from smoking_history_prediction.exception import SmokingHistoryPrediction
import pandas as pd
from typing import Optional
import numpy as np, sys

class SmokingDrinkingData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SmokingHistoryPrediction(e,sys)

    def mongo_collection_to_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise SmokingHistoryPrediction(e,sys)