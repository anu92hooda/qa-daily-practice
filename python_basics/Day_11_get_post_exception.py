import requests


#get with exception handling
def getreq():
    url= "https://reqres.in/api/users"


    try:
        response= requests.get(url ,timeout=5)
        response.raise_for_status()

        data= response.json()
        print("ok" , data)

    except requests.exceptions.HTTPError as h:
        print(h)

    except requests.exceptions.ConnectionError as c:
        print(c)

    except requests.exceptions.Timeout as t:
        print(t)

    except requests.exceptions.RequestException as r:
        print(r)



getreq()


# post with exception handling
def postreq():

    url= "https://reqres.in/api/users"
    payload={
        "name": "Anu",
        "job": "QA Engineer"
    }

    header={
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }

    try:
        response=requests.post(url , headers=header, json=payload)
        response.raise_for_status()

        data=response.json()
        print("OK" , data)

        assert response.status_code== 201
        assert  data["name"] == "Anu"
        assert  data["job"] =="QA Engineer"
        assert "id" in data
        assert "createdAt" in data

    except requests.exceptions.HTTPError as h:
        print(h)

    except requests.exceptions.ConnectionError as c:
        print(c)

    except requests.exceptions.RequestException as e:
        print(e)

postreq()