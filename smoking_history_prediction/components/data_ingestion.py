import os, sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from smoking_history_prediction.entity.config_entity import DataIngestionConfig
from smoking_history_prediction.entity.artifact_entity import DataIngestionArtifact
from smoking_history_prediction.exception import SmokingHistoryPrediction
from smoking_history_prediction.logger import logging
from smoking_history_prediction.dataset_loader.smoking_drinking_data import SmokingDrinkingData


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()) -> None:
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SmokingHistoryPrediction(e, sys)
        
    def export_data_into_csv_files(self)->DataFrame:
        try:
            logging.info(f"Exporting data from mongodb")
            smoking_dataset = SmokingDrinkingData()
            dataframe = smoking_dataset.mongo_collection_to_dataframe(collection_name=
                                                                   self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            exported_data_file_path  = self.data_ingestion_config.exported_csv_file_path
            dir_path = os.path.dirname(exported_data_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {exported_data_file_path}")
            dataframe.to_csv(exported_data_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise SmokingHistoryPrediction(e,sys)
        
    def train_test_split(self,dataframe: DataFrame) ->None:
        logging.info("Entered train_test_split method of DataIngestion class")
        try:
            training_data, testing_data = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info("Exited train_test_split method of DataIngestion class")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Exporting train and test file path.")
            training_data.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            testing_data.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise SmokingHistoryPrediction(e, sys) from e