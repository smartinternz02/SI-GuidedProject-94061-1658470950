import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "0PfVgta9dBanVGQfwxProNK5YPwoEV2M9eup4BBMcIQs"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['a1','a2','a3','a4','a5','a6','a7','Type','Calories','Protien','Fat','Sodium','Fiber','Carbo','Sugars','Potass','Vitamins','Shelf','Weight','Cups'],
                                   "values": [[0,   1,   0,   0,   0,   0,   0,   0,
       100,   2,   1, 140,   2,  11,  10, 120,
        25,   3,   1,   0.75]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d4e19130-c3bf-42f2-aebd-df2d965b4907/predictions?version=2022-08-02', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())