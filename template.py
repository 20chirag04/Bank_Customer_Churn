import os
from pathlib import Path  
import logging

logging.basicConfig(level=logging.INFO,
                     format='%(asctime)s - %(levelname)s - %(message)s')

folders = [
    ".github/workflows",
    "artifacts",
    "config",
    "data",
    "logs",
    "notebooks",
    "src",
    "src/components",
    "src/pipeline",
    "src/entity",
    "src/constants",
    "src/constants/values",
    "templates",
    "static"
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    logging.info(f"Created folder: {folder}")
files = [
    "README.md",
    "requirements.txt",
    "setup.py",
    ".gitignore",
    ".env",
    "app.py",

    "config/schema.yaml",

    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",

    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",

    "src/constants/__init__.py",
    "src/constants/values/__init__.py",


    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/pipeline/predict_pipeline.py",

    "src/entity/artifact_entity.py",
    "src/entity/config_entity.py",

    "templates/index.html"
]
for file in files:

    if not os.path.exists(file):

        with open(file, "w") as f:
            pass

        logging.info(f"Created file: {file}")

    else:
        logging.info(f"{file} already exists")