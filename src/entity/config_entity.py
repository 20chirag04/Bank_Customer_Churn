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


