from datetime import date
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

username = quote_plus(os.getenv("username"))
password = quote_plus(os.getenv("password"))

DATABASE_NAME = "Smoking_History_Prediction"
COLLECTION_NAME = "medical_data"
MONGODB_URL = f"mongodb+srv://{username}:{password}@cluster0.95ipm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

PIPELINE_NAME: str = "smokinghistoryprediction"
ARTIFACT_DIR: str = "artifact"

FILE_NAME: str = "smoking_drinking_dataset.csv"
TRAIN_FILE: str = "train.csv"
TEST_FILE: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "medical_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.3