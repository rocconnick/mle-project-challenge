import hashlib
import json
import requests

payLatePrediction = {
    'loan_amnt': [10000],
    'int_rate': [0.6],
    'purpose': ['credit_card'],
    'grade': ['D'],
    'annual_inc': [20000.00],
    'revol_util': [0.85],
    'emp_length': ['1 year'],
    'dti': [42.00],
    'delinq_2yrs': [4],
    'home_ownership': ['RENT']
    }

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

response = requests.post("http://localhost:5000/predict",
                         data=json.dumps(payLatePrediction),
                         headers=headers)

print(response, response.text)

hash_response = requests.get("http://localhost:5001/getModelHash",
                              data=json.dumps(payLatePrediction),
                              headers=headers)

print(hash_response, hash_response.text)

model_response = requests.get("http://localhost:5001/getModel",
                              data=json.dumps(payLatePrediction),
                              headers=headers)
print(model_response,
      hashlib.sha1(model_response.content).hexdigest() == hash_response.text)
