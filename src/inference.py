import os
import pickle
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to models folder relative to this file
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'rfc.pkl')
MODEL_PATH = os.path.normpath(MODEL_PATH)


with open(MODEL_PATH, 'rb') as f:
    random_forest = pickle.load(f)

class InputSchema(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: int
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int 
    EstimatedSalary: int
    Country: str
    Gender: str

@app.post("/predict")
def predict(predict: InputSchema):
    # One-hot encoding for Country
    country_fr = 1 if predict.Country.lower() == 'france' else 0
    country_ge = 1 if predict.Country.lower() == 'germany' else 0
    country_sp = 1 if predict.Country.lower() == 'spain' else 0

    # One-hot encoding for Gender
    gender_female = 1 if predict.Gender.lower() == 'female' else 0
    gender_male = 1 if predict.Gender.lower() == 'male' else 0

    input_arr = [
        predict.CreditScore,
        predict.Age,
        predict.Tenure,
        predict.Balance,
        predict.NumOfProducts,
        predict.HasCrCard,
        predict.IsActiveMember,
        predict.EstimatedSalary,
        country_fr,
        country_ge,
        country_sp,
        gender_female,
        gender_male
    ]

    ds = pd.DataFrame([input_arr], columns = ['CreditScore',	'Age',	'Tenure',	'Balance',	'NumOfProducts',	'HasCrCard',	'IsActiveMember',	'EstimatedSalary',	'Geography_France',	'Geography_Germany',	'Geography_Spain',	'Gender_Female',	'Gender_Male'])

    if random_forest.predict(ds).item() == 0:
        output = "Not-Leave"
    else:
        output = "Leave"    

    return {"predicted": output}