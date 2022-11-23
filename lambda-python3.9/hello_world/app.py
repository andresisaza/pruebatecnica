import json
import os

# import requests


def lambda_handler(event, context):
    varconfig = os.environ['VARCONFIG']
    print(varconfig)

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hola mundo despliegue isaza",
            # "location": ip.text.replace("\n", "")
        }),
    }
