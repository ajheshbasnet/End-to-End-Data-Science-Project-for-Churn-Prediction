import pandas as pd
import numpy as np
import pickle
from src.inference import app

from fastapi.testclient import TestClient

#------------WITH FASTAPI STUFF---------------------------------#

client = TestClient(app)

def test_chat_endpoint():

    
    input_format = {
        'CreditScore': 658,
        'Age':43,
        'Tenure': 13,
        'Balance': 599999,
        'NumOfProducts':0,
        'HasCrCard': 0,
        'IsActiveMember':1,
        'EstimatedSalary':500000,
        'Country':"Germany",
        'Gender':"MALE"
    }


    response = client.post("/predict", json=input_format)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data['predicted'], str)


# run through "pytest -v filename.py"    