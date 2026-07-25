import streamlit as st
import requests

st.title("Stroke Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.slider("Age", 1, 100, 50)

hypertension = st.selectbox("Hypertension", [0,1])

heart = st.selectbox("Heart Disease",[0,1])

married = st.selectbox("Married",["Yes","No"])

work = st.selectbox(
    "Work Type",
    ["Private","Self-employed","Govt_job","children","Never_worked"]
)

residence = st.selectbox(
    "Residence",
    ["Urban","Rural"]
)

glucose = st.number_input("Average Glucose",50.0,300.0)

bmi = st.number_input("BMI",10.0,60.0)

smoking = st.selectbox(
    "Smoking",
    ["never smoked","formerly smoked","smokes","Unknown"]
)

if st.button("Predict"):

    data = {

        "gender":gender,
        "age":age,
        "hypertension":hypertension,
        "heart_disease":heart,
        "ever_married":married,
        "work_type":work,
        "Residence_type":residence,
        "avg_glucose_level":glucose,
        "bmi":bmi,
        "smoking_status":smoking

    }

    response = requests.post(
         "https://stroke-prediction-ml-si29.onrender.com/predict",
        json=data
    )

    st.write(response.json())

