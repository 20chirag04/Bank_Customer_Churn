from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

class TrainingPipeline:
    def start_training_pipeline(self):
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion(config= data_ingestion_config)

        data_ingestion_artifact = (data_ingestion.data_ingestion_initiate())
