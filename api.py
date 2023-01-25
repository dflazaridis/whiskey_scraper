import requests

PROD_URL = 'https://whiskey-api-c534cunxgq-nw.a.run.app'
LOCAL_URL = 'http://127.0.0.1:5000'
BASE_URL = PROD_URL


def create_new_bottle(whiskey):
    # url of incoming whiskey bottle
    url = whiskey["whiskey_exchange_url"]

    # query firestore db to check if url of incoming bottle already exists
    response = requests.get(f"{BASE_URL}/bottles/?whiskey_exchange_url={url}")

    # if `response returns empty list i.e. bottle does not exist, then post
    if response.text.strip() == "[]":
        requests.post(f"{BASE_URL}/bottles/", json=whiskey)
        return "Bottle created"

    else:
        return "Bottle already exists"


def update_bottle():
    pass
