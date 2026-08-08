import os
import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object
from src.constants import values


class PredictPipeline:
    def __init__(self):
        self.preprocessor_path = os.path.join(
            values.ARTIFACT_DIR,
            values.TRANSFORMED_DIR,
            values.PREPROCESSOR_OBJECT_FILE_NAME
        )

        self.model_path = os.path.join(
            values.ARTIFACT_DIR,
            values.MODEL_TRAINER_DIR,
            values.TRAINED_MODEL_FILE_NAME
        )

    def predict(self, features):
        try:
            preprocessor = load_object(self.preprocessor_path)
            model = load_object(self.model_path)

            transformed_features = preprocessor.transform(features)

            prediction = model.predict(transformed_features)
            probability = model.predict_proba(transformed_features)[:, 1]

            return prediction, probability

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        CreditScore,
        Geography,
        Gender,
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        HasCrCard,
        IsActiveMember,
        EstimatedSalary,
        Satisfaction_Score,
        Card_Type,
        Point_Earned
    ):
        self.CreditScore = CreditScore
        self.Geography = Geography
        self.Gender = Gender
        self.Age = Age
        self.Tenure = Tenure
        self.Balance = Balance
        self.NumOfProducts = NumOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Satisfaction_Score = Satisfaction_Score
        self.Card_Type = Card_Type
        self.Point_Earned = Point_Earned

    def get_data_as_dataframe(self):
        try:
            custom_data_input = {
                "CreditScore": [self.CreditScore],
                "Geography": [self.Geography],
                "Gender": [self.Gender],
                "Age": [self.Age],
                "Tenure": [self.Tenure],
                "Balance": [self.Balance],
                "NumOfProducts": [self.NumOfProducts],
                "HasCrCard": [self.HasCrCard],
                "IsActiveMember": [self.IsActiveMember],
                "EstimatedSalary": [self.EstimatedSalary],
                "Satisfaction Score": [self.Satisfaction_Score],
                "Card Type": [self.Card_Type],
                "Point Earned": [self.Point_Earned]
            }

            return pd.DataFrame(custom_data_input)

        except Exception as e:
            raise CustomException(e, sys)