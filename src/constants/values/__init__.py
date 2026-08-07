import os

## Common Constant Variables used in Data Ingestion
ARTIFACT_DIR = 'artifact'
DATA_DIR = 'data'
RAW_FILE_NAME = 'raw.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'
DATA_FILE_NAME = "Customer-Churn-Records.csv"

## Data Ingestion Variables
TRAIN_TEST_SPLIT_RATIO = 0.2
RANDOM_STATE = 12
INGESTED_DIR = 'data_ingestion'

## Data Validation Variables
VALIDATION_DIR = "data_validation"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml") 
DRIFT_REPORT_FILE_NAME = "drift_report.yaml"

## Data Transformation Variable
TARGET_COLUMN = 'Exited'
TRANSFORMED_DIR = "data_transformation"
TRANSFORMED_TRAIN_FILE_NAME= "train.npy"
TRANSFORMED_TEST_FILE_NAME= "test.npy"
PREPROCESSOR_OBJECT_FILE_NAME= "preprocessor.pkl"


TRAINED_MODEL_DIR = "trained"


EVALUATION_DIR = "evaluation"