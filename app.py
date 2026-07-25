from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

model = joblib.load("stroke_model.joblib")


class StrokeData(BaseModel):

    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str


@app.get("/")
def home():

    return {"message": "Stroke Prediction API"}


@app.post("/predict")
def predict(data: StrokeData):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)

    probability = model.predict_proba(df)

    return {

        "prediction": int(prediction[0]),
        "probability": float(probability[0][1])

    }