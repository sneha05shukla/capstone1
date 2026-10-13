from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("src/model/fraud_model.pkl")

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict():

    sample_data = pd.DataFrame({
        "step": [1],
        "amount": [1000],
        "oldbalanceOrg": [5000],
        "newbalanceOrig": [4000],
        "oldbalanceDest": [0],
        "newbalanceDest": [1000],
        "isFlaggedFraud": [0],
        "type_CASH_OUT": [0],
        "type_DEBIT": [0],
        "type_PAYMENT": [1],
        "type_TRANSFER": [0]
    })

    prediction = model.predict(sample_data)

    return {"prediction": int(prediction[0])}
