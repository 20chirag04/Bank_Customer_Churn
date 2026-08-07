import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

from src.constants import values


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Ingestion Initiated")
            print("Ingestion Started")

            df = pd.read_csv(self.config.data_path)

            os.makedirs(self.config.artifact_dir,exist_ok=True)
            os.makedirs(self.config.ingested_dir,exist_ok=True)
            
            df.to_csv(self.config.raw_file_path,index=False)

            train_df,test_df = train_test_split(df,
                                            test_size=values.TRAIN_TEST_SPLIT_RATIO,
                                            random_state=values.RANDOM_STATE)

            train_df.to_csv(self.config.train_file_path,index = False)
            test_df.to_csv(self.config.test_file_path,index = False)

            logging.info("Ingestion Completed")
            return DataIngestionArtifact(
                train_data_path=self.config.train_file_path,
                test_data_path=self.config.test_file_path,
                raw_data_path=self.config.raw_file_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)
