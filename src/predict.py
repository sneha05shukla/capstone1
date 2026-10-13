import joblib
import pandas as pd

# Load model
model = joblib.load("src/model/fraud_model.pkl")

# Sample transaction
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

# Prediction
prediction = model.predict(sample_data)

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Fraud Transaction")
else:
    print("Legitimate Transaction")