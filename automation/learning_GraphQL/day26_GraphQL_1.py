
import requests
import json

from automation.learning_GraphQL.day25_GraphQL_inpython import header, payload

url="https://graphqlzero.almansi.me/api"

introspection_query='''
{
__type(name: "Post"){
   name
   fields  {
   name
         }
      }
   }

'''

headers= {
            "Content-Type": "application/json"
        }
payload= {
    "query": introspection_query
}


def test_post_has_expected_fields():
    try:
        response= requests.post(url, json= payload, headers=headers)

        assert response.status_code in [200, 201] , "Request failed"

        data= response.json()
        print(json.dumps(data, indent=2))

    except Exception as e:
        print("there is an error", e)

    finally:
        print("completed please check execution")