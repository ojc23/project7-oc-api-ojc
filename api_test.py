import requests
import pandas as pd
import requests, json
import ast

# https://fastapi.tiangolo.com/fr/tutorial/first-steps/

url = 'http://127.0.0.1:8000/predict/'

#def prediction(self, id_client):
def prediction():
    #url ="https://fastapi-avi-oc-projet7.herokuapp.com/predict"
    url ='http://127.0.0.1:8000/predict'
    #data_to_predict = self.data[self.data["SK_ID_CURR"] == id_client].drop(['SK_ID_CURR', 'TARGET'], axis = 1)
    #data_to_predict = pd.DataFrame(self.data.drop(['SK_ID_CURR', 'TARGET'], axis = 1).iloc[id]).T
    #data_to_predict_json = json.dumps(data_to_predict.to_dict('records')[0])
    
    #response = requests.request("POST", url, headers=headers)
    #url = 'https://www.w3schools.com/python/demopage.php'
    


    #myobj = {'proba_computed': 'somevalue'}
    #x = requests.post(url, json = myobj)
    # Making a POST request
    r = requests.post(url, data ={'proba_computed'})
    # check status code for response received
    # success code - 200
    print(r)
 
    # print content of request
    print(r.json())

   
    #response = requests.request("POST", url)
    #response = requests.post(url)
    #proba = pd.read_json(response.json()) 
    #proba = float(ast.literal_eval(response.text)["proba_failed"])
    
    #proba = float(ast.literal_eval(response.text)["proba_computed"])
    
    #print(response)
    
    #if proba > 0.7:
    #    message = "La probabilité de non remboursement est de: "
    #    result = "Ce client est à risque"
    #else:
    #    message = "La probabilité de remboursement est de: "
    #    result = "Client éligible au prêt"
    #    proba = 1 - proba

    #print (proba, result, message)
    #return (proba, result, message)


prediction() 

