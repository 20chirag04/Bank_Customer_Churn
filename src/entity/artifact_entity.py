from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_data_path:str
    test_data_path:str
    raw_data_path:str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    drift_report_file_path: str
    message: str