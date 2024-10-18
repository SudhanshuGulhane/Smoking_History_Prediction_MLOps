import sys
from smoking_history_prediction.exception import SmokingHistoryPrediction
from smoking_history_prediction.logger import logging
from smoking_history_prediction.components.data_ingestion import DataIngestion
from smoking_history_prediction.entity.config_entity import DataIngestionConfig
from smoking_history_prediction.entity.artifact_entity import DataIngestionArtifact

class TrainingPipeLine:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train data and test data from mongodb")
            return data_ingestion_artifact
        except Exception as e:
            raise SmokingHistoryPrediction(e, sys) from e
        
    def run_pipeline(self, ) -> None:
        try:
            data_ingestion_artifact = self.data_ingestion()
        except Exception as e:
            raise SmokingHistoryPrediction(e, sys) from e