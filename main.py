from typing import Union
from fastapi import FastAPI
from validator import Validador
from prediction import predict_well_conditions

import pickle

from input_predict import Input_Validation

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Bienvenidos a mi servidor en mi pc'}


@app.post('/predict')
def model_predict(data:Validador):
    return predict_well_conditions(data)