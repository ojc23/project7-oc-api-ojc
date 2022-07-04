# -*- coding: utf-8 -*-
from flask import Flask
import pickle
import pandas as pd
import ast
import json

app = Flask(__name__)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.route('/')
def index():
    return {'message': 'Hello, API for Credit scoring ojc'}

@app.route("/predict/")
def predict():
    # load the model from disk
    filename = r'./model.pkl'
    model = pickle.load(open(filename, 'rb'))

    #Load Dataframe
    x_test = pd.read_csv('./x_test.csv', nrows=100).set_index('SK_ID_CURR')
        
    probas = model.predict_proba(x_test)[:,1]
    dict_proba = {'proba_computed': str(probas[0])}
    json_ = json.dumps(dict_proba)

    print(json_)
    #return json_
    return dict_proba


# http://localhost:5000/
if __name__ == "__main__":
    app.run(debug=True)