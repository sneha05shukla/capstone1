import sys
import os

sys.path.append(os.path.abspath("."))

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict():
    payload = {
        "step": 1,
        "amount": 1000,
        "oldbalanceOrg": 5000,
        "newbalanceOrig": 4000,
        "oldbalanceDest": 0,
        "newbalanceDest": 1000,
        "isFlaggedFraud": 0,
        "type_CASH_OUT": 0,
        "type_DEBIT": 0,
        "type_PAYMENT": 1,
        "type_TRANSFER": 0
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
