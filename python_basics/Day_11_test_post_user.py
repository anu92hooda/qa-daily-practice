import requests

url= "https://reqres.in/api/users"

# create a Python dictionary with the data we want to send
payload={
    "name":"Anu",
    "job":"QA Engineer"
    }
header= {
    "Content-Type": "application/json",
    "x-api-key": "reqres-free-v1"   # ⬅️ match Postman header
}

# send the post request to server with data as JSON
response= requests.post(url, headers=header, json=payload)

#print the status code , Expected 201 created
print("Status code", response.status_code)

# convert the data to JSON format(dict)
data= response.json()
print("Response Body:", data)

# Test the output with assert
assert response.status_code == 201
assert data["name"] == "Anu"
assert  data["job"] == "QA Engineer"
assert  "id" in data
assert "createdAt" in data