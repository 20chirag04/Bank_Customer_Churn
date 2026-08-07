import os
from src.constants import values

class DataIngestionConfig:
    def __init__(self):
        self.artifact_dir = values.ARTIFACT_DIR
        
        self.ingested_dir = os.path.join(values.ARTIFACT_DIR,values.INGESTED_DIR)
        self.raw_file_path = os.path.join(self.ingested_dir,values.RAW_FILE_NAME)
        self.train_file_path = os.path.join(self.ingested_dir,values.TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.ingested_dir,values.TEST_FILE_NAME)
        self.data_path = os.path.join(values.DATA_DIR,values.DATA_FILE_NAME)
        self.train_test_split_ratio = values.TRAIN_TEST_SPLIT_RATIO

class DataValidationConfig:
    def __init__(self):
        
        self.validation_dir = os.path.join(values.ARTIFACT_DIR,values.VALIDATION_DIR)
        self.drift_report_file_path = os.path.join(self.validation_dir,values.DRIFT_REPORT_FILE_NAME)
        self.schema_file_path = values.SCHEMA_FILE_PATH

class DataTransformationConfig:
    def __init__(self):
        self.transformed_dir = os.path.join(values.ARTIFACT_DIR,values.TRANSFORMED_DIR)
        self.transformed_train_file_path = os.path.join(self.transformed_dir,values.TRANSFORMED_TRAIN_FILE_NAME)
        self.transformed_test_file_path = os.path.join(self.transformed_dir,values.TRANSFORMED_TEST_FILE_NAME)
        self.preprocessor_object_file_path = os.path.join(self.transformed_dir,values.PREPROCESSOR_OBJECT_FILE_NAME)
        


