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

print(response)
print(response, response.text)
