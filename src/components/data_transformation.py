import os
import sys
import yaml
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,read_yaml,save_numpy_array
from src.entity.artifact_entity import DataIngestionArtifact,DataTransformationArtifact
from src.entity.config_entity import DataTransformationConfig
from src.constants import values

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig,
                data_ingestion_artifact:DataIngestionArtifact):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifact = data_ingestion_artifact
    
    def get_data_transformer_object(self):
        try:
            logging.info("Creating Data Transformation Pipeline")

            self.schema_config = read_yaml(values.SCHEMA_FILE_PATH)

            numerical_column = self.schema_config["numerical_columns"]
            categorical_column = self.schema_config["categorical_columns"]
            ordinal_column = self.schema_config["ordinal_columns"]

            num_pipeline = Pipeline(
                steps= [
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('OneHotEncoding',OneHotEncoder(drop='first',handle_unknown='ignore')),
                    ('imputer',SimpleImputer(strategy='most_frequent'))
                ]
            )
            ordinal_pipeline = Pipeline(
                steps=[
                    ('Ordinal Encoding',OrdinalEncoder())
                ]
            )
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline',num_pipeline,numerical_column),
                    ('categorical_pipeline',cat_pipeline,categorical_column),
                    ('ordinal_pipeline',ordinal_pipeline,ordinal_column)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_data_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_data_path)
            target_column = values.TARGET_COLUMN

            X_train = train_df.drop(columns=target_column)
            y_train = train_df[target_column]
            X_test = test_df.drop(columns=target_column)
            y_test = test_df[target_column]

            preprocessor = self.get_data_transformer_object()

            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

            train_arr = np.c_[X_train,np.array(y_train)]
            test_arr = np.c_[X_test,np.array(y_test)]

            save_numpy_array(self.data_transformation_config.transformed_train_file_path,train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path,test_arr)
            save_object(self.data_transformation_config.preprocessor_object_file_path,preprocessor)

            logging.info("Data Transformation Successful")

            return DataTransformationArtifact(
                preprocessor_object_file_path= self.data_transformation_config.preprocessor_object_file_path,
                transformed_train_file_path= self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path= self.data_transformation_config.transformed_test_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)