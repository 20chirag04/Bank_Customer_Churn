from src.logger import logging
from src.exception import CustomException
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import (
    DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
    )

class TrainingPipeline:
    def start_training_pipeline(self):
        try:
            data_ingestion_config = DataIngestionConfig()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion_artifact = (data_ingestion.initiate_data_ingestion())
            logging.info("Ingestion Successful")


            data_validation_config = DataValidationConfig()
            data_validation = DataValidation(
                data_validation_config=data_validation_config,
                data_ingestion_artifact=data_ingestion_artifact
            )
            data_validation_artifact = (data_validation.initiate_data_validation())
            logging.info(f"Validation Message : {data_validation_artifact.message}")
            logging.info(f"Validation Status :{data_validation_artifact.validation_status}")

            data_transformation_config = DataTransformationConfig()
            data_transformation = DataTransformation(
                                                    data_ingestion_artifact=data_ingestion_artifact,
                                                    data_transformation_config=data_transformation_config
            )
            data_transformation_artifact = (data_transformation.initiate_data_transformation())

            model_trainer_config = ModelTrainerConfig()
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                         model_trainer_config=model_trainer_config)
            model_trainer_artifact = (model_trainer.initiate_model_trainer())

        except Exception as e:
            raise CustomException(e,sys)