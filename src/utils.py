import os
import sys
import dill
import yaml
from src.logger import logging
from src.exception import CustomException

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