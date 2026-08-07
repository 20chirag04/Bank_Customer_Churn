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


TRANSFORMED_DIR = "transformed"

TRAINED_MODEL_DIR = "trained"

VALIDATION_DIR = "validation"

EVALUATION_DIR = "evaluation"