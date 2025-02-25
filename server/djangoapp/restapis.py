import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Get backend URL and sentiment analyzer URL from environment variables.
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"
    # If there are URL parameters, append them; otherwise, just use the endpoint.
    request_url = backend_url + endpoint + ("?" + params if params else "")
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Network exception occurred: ", e)
        return None

def analyze_review_sentiments(text):
    # Construct the URL for sentiment analysis. (You may want to URL-encode the text if needed.)
    request_url = sentiment_analyzer_url + "analyze/" + text
    print("GET sentiment from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None

def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    print("POST to {} with data: {}".format(request_url, data_dict))
    try:
        response = requests.post(request_url, json=data_dict)
        print("Response: ", response.json())
        return response.json()
    except Exception as e:
        print("Network exception occurred: ", e)
        return None
