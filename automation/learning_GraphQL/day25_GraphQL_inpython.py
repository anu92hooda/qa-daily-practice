import  requests
import  json

from selenium.webdriver.common.devtools.v136.dom import query_selector

from python_basics.Day_11_test_post_user import payload

url= "https://graphqlzero.almansi.me/api"

# GraphQL mutation (as string)
mutation= """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    id
    title
    body
  }
}
"""

# Variable to pass
variables= {
    "input":{
        "title": "Post from Python",
        "body": "This was sent using Python + GraphQL variables!"
    }
  }

# Headers
header= {
    "Content-Type": "application/json"

}

payload= {
    "query": mutation,
    "variables": variables
}

# send the request
response= requests.post(url, json=payload, headers=header)

if response.status_code == 200:
    print("success")
    print(json.dumps(response.json(), indent=2))

else:
    print("failed")







