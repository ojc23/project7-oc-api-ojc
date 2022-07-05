import pandas as pd
import requests, json
import ast

#Test locally type
# heroku local
# url ='http://127.0.0.1:5000/'
# https://project7-api-ojc.herokuapp.com/?id_custo=50

#def prediction(self, id_client):
def prediction(id_custo):
    #url ='https://project7-api-ojc-s.herokuapp.com'
    #url ='http://127.0.0.1:8000/predict/'
    url ='http://127.0.0.1:5000/'

    headers = {'Content-Type': 'application/json'}

    headers = {
    'Accept': 'application/json',
    'Authorization': 'key ttn-account-notsharinganything',
        }
        
    params = {
        'running': True,
        'id_custo': id_custo,
    }

    #https://www.thethingsnetwork.org/forum/t/send-get-request-with-python-curl-with-requests-package-to-swagger-api/44436 
    response = requests.get(url, headers=headers, params=params)
    print(response)
    print(response.json())
    proba = float(ast.literal_eval(response.text)["proba_computed"])
    print(proba)

if __name__ == '__main__':
    prediction(id_custo = 22) 

