# -*- coding: utf-8 -*-
from flask import Flask
import pickle
import pandas as pd


app = Flask(__name__)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.route('/')
def index():
    return {'message': 'Hello, API for Credit scoring'}

@app.route("/predit")
def preditc():
    # load the model from disk
    filename = r'../notebook/model.pkl'
    model = pickle.load(open(filename, 'rb'))

    #Load Dataframe
    path_df = '../notebook/x_test.csv'
    #x_test = pd.read_csv(path_df, index_col=0, nrows=20)
    x_test = pd.read_csv('../notebook/x_test.csv', nrows=100).set_index('SK_ID_CURR')
    y_test = pd.read_csv('../notebook/x_test.csv', nrows=100).set_index('SK_ID_CURR')
        
    probas = model.predict_proba(x_test)[:,1]

    return {'proba_failed': str(probas[0])}


# http://localhost:5000/
if __name__ == "__main__":
    app.run()