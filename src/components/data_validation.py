import os 
import sys
import pandas as pd 

from src.logger import logging
from src.exception import CustomException
from src.utils import read_yaml
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

class DataValidation:
        def __init__(
            self,
            data_validation_config:DataValidationConfig,
            data_ingestion_artifact: DataIngestionArtifact
        ):
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

            self.schema_config = read_yaml(
                self.data_validation_config.schema_file_path
            )
            
            os.makedirs(self.data_validation_config.validation_dir,exist_ok=True)

        def validate_number_of_columns(self,dataframe):
            logging.info("Validating Number of Columns")
            expected_columns = self.schema_config['columns']

            if len(dataframe.columns) != len(expected_columns):
                return False
        
            return True
        
        def validate_column_names(self,dataframe):
            logging.info("Validating Names of Columns")
            expected_columns = self.schema_config['columns']

            for name in expected_columns:
                if name not in dataframe.columns:
                    logging.info(f"Missing Column : {name}")
                    return False
            return True
        
        def validate_dataset_schema(self,dataframe):
            logging.info("Validating Dataset Schema")

            if not self.validate_number_of_columns(dataframe):
                return False
            if not self.validate_column_names(dataframe):
                return False
            return True
        
        def detect_data_drift(self, reference_df, current_df):
            try:
                report = Report(metrics=[DataDriftPreset()])
                report.run(reference_data=reference_df,current_data=current_df)
                os.makedirs(
                    self.data_validation_config.validation_dir,
                    exist_ok=True
                )

                report.save_html(
                    self.data_validation_config.drift_report_file_path
                )

                logging.info("Drift report generated successfully.")
                return True
            except Exception as e:
                raise CustomException(e, sys)
            
        def initiate_data_validation(self):
            try:
                logging.info("Initialising Data Validation")
                train_df = pd.read_csv(self.data_ingestion_artifact.train_data_path)        
                test_df = pd.read_csv(self.data_ingestion_artifact.test_data_path)  

                train_status = self.validate_dataset_schema(train_df)
                test_status = self.validate_dataset_schema(test_df)
                drift_status = self.detect_data_drift(train_df,test_df)

                drift_report_file_path = self.data_validation_config.drift_report_file_path

                validation_status = (train_status and test_status and drift_status)      

                return DataValidationArtifact(drift_report_file_path=drift_report_file_path,
                                            validation_status=validation_status,
                                            message=(
                                                "validation successful"
                                                if validation_status
                                                else "validation Failed"
                                            ))
            except Exception as e:
                raise CustomException(e,sys)