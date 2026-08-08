import os
import sys
import dill
import yaml
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import recall_score,accuracy_score,precision_score,roc_auc_score,f1_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, 'wb') as file :
            dill.dump(obj,file)

        logging.info(f"Object {obj} saved successfully at {file_path}")

    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file :
            obj = dill.load(file)
        
        logging.info(f"Object Loaded Successfully from {file_path}")

        return obj
    except Exception as e:
        raise CustomException(e,sys)

def read_yaml(file_path):
    try:
        with open(file_path,'r') as file:
            content = yaml.safe_load(file)

        logging.info(f'Successfully read Yaml file {file_path}')

        return content
    except Exception as e:
            raise CustomException(e,sys)

def save_numpy_array(file_path ,array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise CustomException(e,sys)


def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for model_name, model in models.items():
            logging.info(
                f"Hyperparameter tuning started for {model_name}"
            )
            para = param[model_name]

            gs = GridSearchCV(model,para,cv=3,verbose=2,
                scoring="recall",n_jobs=-1)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = recall_score(y_train, y_train_pred)

            test_model_score = recall_score(y_test, y_test_pred)

            report[model_name] = test_model_score

            logging.info(
                f"{model_name} Recall: "
                f"{test_model_score}"
            )
            logging.info(f"Best Parameters: {gs.best_params_}")
            models[model_name] = model
        return report
    except Exception as e:
        raise CustomException(e, sys)

def classification_metrics(model,true ,predicted,x_val ):
    accuracy = accuracy_score(true,predicted)
    precision = precision_score(true ,predicted)
    recall = recall_score(true ,predicted)
    f1 = f1_score(true ,predicted)
    y_probability = model.predict_proba(x_val)[:, 1]
    roc_auc = roc_auc_score(true, y_probability)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "roc_auc": roc_auc
    }