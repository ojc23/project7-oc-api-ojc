# -*- coding: utf-8 -*-
#from flask import Flask
#import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd


# 1. to run use : python3 api.py 

#app = Flask(__name__)
app = FastAPI()

# 2. Index route, opens automatically on http://127.0.0.1:5000
@app.get('/')
def index():
    return {'message': 'Hello, API for Credit scoring'}

# 3. Define the prediction function, make a prediction from the datase
#    and return the predicted 
@app.post("/predit")
def preditc():
    # load the model from disk
    filename = r'./model.pkl'
    model = pickle.load(open(filename, 'rb'))

    #Load Dataframe
    path_df = './x_test.csv'
    x_test = pd.read_csv('./x_test.csv', nrows=100).set_index('SK_ID_CURR')
        
    probas = model.predict_proba(x_test)[:,1]

    return {'proba_failed': str(probas[0])}


# http://localhost:5000/
if __name__ == '__main__':
    #uvicorn.run(app, host='127.0.0.1', port=5000)
    uvicorn app.api:app
