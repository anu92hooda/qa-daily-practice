

# Mock Response
response={
    "status":"success",
    "token":"abctest",
    "user":{
        "id":101,
        "name":"Anu QA",
        "role":"tester"
        }
    }

print(response["status"])
print(response["user"]["name"])

# check id Key exists or valid

if "token" in response:
    print("Auth token valid")
else:
    print("Auth token invalid")


#looping through dictionary

for k,v in response.items():
    print(f"{k}:{v}")


