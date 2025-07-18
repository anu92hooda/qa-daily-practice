from logging import exception

import requests
import json

from automation.learning_GraphQL.day25_GraphQL_inpython import header, variables


def day25():
    try:
        url= "https://graphqlzero.almansi.me/api"

        mutation= '''
            mutation CreatePost($input1: CreatePostInput!, $input2: CreatePostInput! ) {
            first: createPost(input: $input1) {
                 title
                 body
                 id
                                       }
            second: createPost(input: $input2){
                 title
                 body
                 id
            }
                         } '''

        variables= {
            "input1":{
                "title": "Post from Python Data 1",
                "body": "This was sent using Python + GraphQL variables!"
             },
            "input2": {
                "title": "Post from Python Data 2",
                "body": "This was sent using Python + GraphQL variables!"
            }
            }

        headers= {
            "Content-Type": "application/json"
        }

        payload = {
            "query":mutation ,
            "variables":variables
            }

        response=requests.post(url, json=payload, headers=headers)
        data= response.json()
        print(json.dumps(data, indent=2))

        if "errors" in data:
            print(" Error occurred")
            for e in data["errors"]:
                print(f"error message {e}")


        assert "data" in data , "Missing 'data' key"
        assert  "first" in data["data"] , "Missing 'first' "
        assert  "second" in data["data"] , "Missing 'second' "
        first_post= data["data"]["first"]
        second_post = data["data"]["second"]

        assert first_post["id"] , "Missing first Post ID"
        assert first_post["title"] == variables["input1"]["title"] , "Title mismatched"
        assert first_post["body"] == variables["input1"]["body"] , "Body mismatched"

    except exception as er:
        print(f"error is {er}")

    finally:
        print(" test completed please check response in result report ")

day25()








