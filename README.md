# Bank Customer Churn Prediction

A machine learning project that predicts whether a bank customer is likely to leave the bank based on their personal and account information.

The main goal of this project was not only to build a classification model, but also to build the project using a proper ML project structure with separate components for data ingestion, validation, transformation, model training, and prediction.

## Project Overview

Customer churn is an important problem for banks because retaining an existing customer is generally more valuable than acquiring a new one.

In this project, I built a binary classification pipeline that predicts:

- `0` → Customer is likely to stay
- `1` → Customer is likely to churn

The project also includes a Streamlit interface where users can enter customer details and get a prediction along with the churn probability.

## Dataset

The dataset contains information about bank customers such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card status
- Active Member status
- Estimated Salary
- Satisfaction Score
- Card Type
- Points Earned

The target variable is:

```text
Exited