# -*- coding: utf-8 -*-
#from flask import Flask
import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd
#from fastapi.responses import UJSONResponse
# pip install "fastapi[all]"  to return json format
from fastapi.responses import ORJSONResponse  
import streamlit as st

'''
this scrip define the API to provide the score of 
one customer to the application
tu ru : uvicorn main:app --reload
'''

from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict/", response_class=ORJSONResponse)
def predict():
    # load the model from disk
    filename = r'model.pkl'
    model = pickle.load(open(filename, 'rb'))

    #Load Dataframe
    x_test = pd.read_csv('x_test.csv', nrows=100).set_index('SK_ID_CURR')
        
    probas = model.predict_proba(x_test)[:,1]

    st.json({'proba_computed': str(probas[7])})

    return {'proba_computed': str(probas[7])}
    #return {'proba_computed': str(probas)}



#if __name__ == "__main__":
#    uvicorn.run("main:app", port=8000, workers=1)



