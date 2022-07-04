import pandas as pd
import requests, json
import ast


#def prediction(self, id_client):
def prediction():
    #url ="https://ojc23-project7-oc-api-ojc-main-6h08ks.streamlitapp.com/predict"
    url ="https://fastapi-avi-oc-projet7.herokuapp.com/predict"
    #url ='http://127.0.0.1:8000/predict/'
    headers = {'Content-Type': 'application/json'}

    headers = {
    'Accept': 'application/json',
    'Authorization': 'key ttn-account-notsharinganything',
        }

    params = (('proba_computed', 'proba'),)
    #https://www.thethingsnetwork.org/forum/t/send-get-request-with-python-curl-with-requests-package-to-swagger-api/44436 
    response = requests.get(url, headers=headers, params=params)
    print(response)
    print(response.json())
    proba = float(ast.literal_eval(response.text)["proba_computed"])
   
    print (proba)
    return (proba)


prediction() 

