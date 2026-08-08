import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.entity.artifact_entity import DataTransformationArtifact
from src.entity.artifact_entity import ModelTrainerArtifact


st.set_page_config(page_title="Bank Customer Churn Prediction",
                   page_icon="🏦")
st.title("Bank Customer Churn Prediction")
st.write("Enter customer details to predict churn.")

st.subheader("Customer Information")

CreditScore = st.number_input("Credit Score",min_value=300,max_value=850,value=650)

Geography = st.selectbox("Geography",["France", "Germany", "Spain"])

Gender = st.selectbox("Gender",["Male", "Female"])

Age = st.number_input("Age",min_value=18,max_value=100,value=35)

Tenure = st.number_input("Tenure",min_value=0,max_value=10,value=5)
Balance = st.number_input("Balance",min_value=0.0,value=500000.0)

NumOfProducts = st.number_input("Number of Products",min_value=1,max_value=4,value=1)

HasCrCard = st.selectbox("Has Credit Card",[0, 1])

IsActiveMember = st.selectbox("Is Active Member",[0, 1])

EstimatedSalary = st.number_input("Estimated Salary",min_value=0.0,value=500000.0)
Satisfaction_Score = st.number_input("Satisfaction Score",min_value=1,max_value=5,value=3)

Card_Type = st.selectbox("Card Type",["DIAMOND", "GOLD", "PLATINUM", "SILVER"])

Point_Earned = st.number_input("Point Earned",min_value=0,value=500)

if st.button("Predict Churn"):
    custom_data = CustomData(
        CreditScore=CreditScore,
        Geography=Geography,
        Gender=Gender,
        Age=Age,
        Tenure=Tenure,
        Balance=Balance,
        NumOfProducts=NumOfProducts,
        HasCrCard=HasCrCard,
        IsActiveMember=IsActiveMember,
        EstimatedSalary=EstimatedSalary,
        Satisfaction_Score=Satisfaction_Score,
        Card_Type=Card_Type,
        Point_Earned=Point_Earned
    )

    features = custom_data.get_data_as_dataframe()

    predict_pipeline = PredictPipeline()

    prediction, probability = predict_pipeline.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")

    st.write(f"Churn Probability: {probability[0]:.2%}")

