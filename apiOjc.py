# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd
from fastapi.responses import ORJSONResponse  
from fastapi import FastAPI

app = FastAPI(title="Provide credit score fro a customer",
              version="0.1.0",)

@app.get("/", response_class=ORJSONResponse)
def predict(id_custo:int):
    # load the model from disk
    filename = r'model.pkl'
    model = pickle.load(open(filename, 'rb'))

    #Load Dataframe
    x_test = pd.read_csv('x_test.csv', nrows=100).set_index('SK_ID_CURR')
        
    probas = model.predict_proba(x_test)[:,1]

    return {'proba_computed': str(probas[id_custo])}

#if __name__ == "__main__":
#    uvicorn.run("main:app", port=8000, workers=1)



