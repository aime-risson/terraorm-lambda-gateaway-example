import json
def mainFoo(e,f):
    response = {
    "statusCode": 200,
    "body": json.dumps("hello world"),
    "headers": {
        "Content-Type": "application/json"
    }
    }
    return response