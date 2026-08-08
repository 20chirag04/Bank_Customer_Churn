import os
import sys
import numpy as np

from src.constants import values
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,evaluate_models,classification_metrics
from src.entity.artifact_entity import (DataTransformationArtifact,ModelTrainerArtifact)
from src.entity.config_entity import ModelTrainerConfig

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from imblearn.over_sampling import SMOTE

class ModelTrainer:
    def __init__(self,
        data_transformation_artifact:DataTransformationArtifact,
        model_trainer_config:ModelTrainerConfig
        ):
        self.model_trainer_config = model_trainer_config
        self.data_transformation_artifact = data_transformation_artifact        

    def train_model(self):
        try:
            logging.info("model training initiated")

            train_arr = np.load(self.data_transformation_artifact.transformed_train_file_path)
            test_arr = np.load(self.data_transformation_artifact.transformed_test_file_path)
            
            X_train= train_arr[:,:-1]
            y_train= train_arr[:,-1]

            X_test= test_arr[:,:-1]
            y_test= test_arr[:,-1]

            smote = SMOTE(random_state = 12)

            X_train_smote,y_train_smote = smote.fit_resample(X_train,y_train) # type: ignore[assignment]

            models = {
                "RandomForest": RandomForestClassifier(random_state=12),
                "DecisionTree": DecisionTreeClassifier(random_state=12),
                "GradientBoosting": GradientBoostingClassifier(random_state=12)
            }
            params = {
                'RandomForest': {
                    "n_estimators": [100, 200, 300, 500],
                    "max_depth": [None, 10, 20, 30],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 4],
                },
                "DecisionTree": {
                    # "criterion": ["gini", "entropy", "log_loss"],
                    "max_depth": [ 5, 10, 15, 20, 30],
                    "min_samples_split": [2, 5, 10, 20],
                    "min_samples_leaf": [1, 2, 4, 8],
                },
                "GradientBoosting":{
                    "n_estimators": [100, 200, 300],
                    "learning_rate": [0.01, 0.05, 0.1, 0.2],
                    "max_depth": [2, 3, 4, 5],
                    # "min_samples_split": [2, 5, 10],
                    # "min_samples_leaf": [1, 2, 4],
                }
            }
            model_report:dict = evaluate_models(
                 X_test=X_test,X_train=X_train_smote,y_test=y_test,y_train=y_train_smote,models=models,param=params)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))
    
            ## To get best model name from dict
            best_model_name = list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                ]
            best_model = models[best_model_name]

            y_train_pred=best_model.predict(X_train)

            logging.info(f"Best Model is {best_model_name} with Recall Score : {best_model_score}")

            classification_train_metric=classification_metrics(true=y_train,predicted=y_train_pred,x_val=X_train,model=best_model)
    
            y_test_pred=best_model.predict(X_test)
            classification_test_metric=classification_metrics(true=y_test,predicted=y_test_pred,x_val=X_test,model=best_model)  
            logging.info(
                f"Final Test Metrics: {classification_test_metric}"
            )
            os.makedirs(self.model_trainer_config.model_trainer_dir,exist_ok=True)
            save_object(self.model_trainer_config.trained_model_file_path,best_model) 

            model_trainer_artifact = ModelTrainerArtifact(
                 trained_model_file_path=self.model_trainer_config.trained_model_file_path
            )
            return model_trainer_artifact
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_model_trainer(self):   
        try:                 
            self.model_trainer_artifact = self.train_model()
            return self.model_trainer_artifact
        except Exception as e:
                    raise CustomException(e,sys)