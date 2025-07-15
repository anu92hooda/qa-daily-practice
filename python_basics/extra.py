import requests
import json

url= "https://reqres.in/api/users"

response= requests.get(url, timeout=10)
response.raise_for_status()

status =response.status_code
data=response.json()

assert "user" in data
assert "Id" in data
assert  status =="201"

with open("data1.json",'w') as file:
    json.dump(data ,file , indent=4)

with open("data1.json",'r') as file:
    dta1= json.load(file)
    print(dta1["user"])

