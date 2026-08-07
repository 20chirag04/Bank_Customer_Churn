from src.logger import logging
from src.exception import CustomException
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig

class TrainingPipeline:
    def start_training_pipeline(self):
        try:
            data_ingestion_config = DataIngestionConfig()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion_artifact = (data_ingestion.data_ingestion_initiate())
            logging.info("Ingestion Successful")


            data_validation_config = DataValidationConfig()
            data_validation = DataValidation(
                data_validation_config=data_validation_config,
                data_ingestion_artifact=data_ingestion_artifact
            )
            data_validation_artifact = (data_validation.initiate_data_validation())
            logging.info(f"Validation Message : {data_validation_artifact.message}")
            logging.info(f"Validation Status :{data_validation_artifact.validation_status}")
        except Exception as e:
            raise CustomException(e,sys)