# -*- coding: utf-8 -*-
#from flask import Flask
import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict/")
def predict():
    # load the model from disk
    filename = r'model.pkl'
    model = pickle.load(open(filename, 'rb'))

    #Load Dataframe
    x_test = pd.read_csv('x_test.csv', nrows=100).set_index('SK_ID_CURR')
        
    probas = model.predict_proba(x_test)[:,1]

    return {'proba_computed': str(probas[1])}
