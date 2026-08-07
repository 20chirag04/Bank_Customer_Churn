import os

## Common Constant Variables used in Data Ingestion
ARTIFACT_DIR = 'artifact'
DATA_DIR = 'data'
RAW_FILE_NAME = 'raw.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'
DATA_FILE_NAME = "Customer-Churn-Records.csv"
TARGET_COLUMN = 'Exited'

## Data Ingestion Variables
TRAIN_TEST_SPLIT_RATIO = 0.2
RANDOM_STATE = 12
INGESTED_DIR = 'data_ingestion'

## Data Validation Variables
VALIDATION_DIR = "data_validation"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml") 
DRIFT_REPORT_FILE_NAME = "drift_report.yaml"


TRANSFORMED_DIR = "transformed"

TRAINED_MODEL_DIR = "trained"


EVALUATION_DIR = "evaluation"