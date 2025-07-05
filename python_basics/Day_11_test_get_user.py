import requests

# send a Get request
url="https://reqres.in/api/users/2"
response=requests.get(url)


# Print the status code (should be 200)
print("status code:",response.status_code)

#print the response body as JSON
print("Response Body:",response.json())

#Add a test - check if email ends with 'reqres.in'
data= response.json()
assert data['data']['email'].endswith('reqres.in')