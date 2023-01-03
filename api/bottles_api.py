import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

from .bottles import Bottle, bottleFromRequest
from .utils import BOTTLE_ROUTES

from .bottles.models import example_bottle


db = firestore.client()
bottles_col = db.collection('bottles')
bottles_api = Blueprint('bottles_api', __name__)


@bottles_api.route(BOTTLE_ROUTES['create'].path, methods=BOTTLE_ROUTES['create'].methods)
def create_bottle():
    """
    Create a new bottle of whiskey in the database
    """
    data = request.json

    # Convert data to bottle
    bottle = bottleFromRequest(data=data)
    res = bottles_col.document().set(bottle.to_json())
    print(str(res))

    # return bottle.to_json()
    return "Bottle created"


# Todo: Implement list
@bottles_api.route(BOTTLE_ROUTES['list'].path, methods=BOTTLE_ROUTES['list'].methods)
def list_bottles():
    """
    List the first 10 whiskey bottles in the database by price
    """
    bottles_query = bottles_col.order_by(
        'price', direction='DESCENDING').stream()
    results = [bottles.to_dict() for bottles in bottles_query]

    bottles_list = [[bottle['name'], f'{bottle["currency"]}{bottle["price"]}']
                    for bottle in results]

    return str(bottles_list)

# Todo: Implement get


@bottles_api.route(BOTTLE_ROUTES['get'].path, methods=BOTTLE_ROUTES['get'].methods)
def get_bottle(bottle_id: str):
    """
    Get bottle details by id
    """

    bottle = bottles_col.document(bottle_id).get()

    return bottle.to_dict()


# Todo: Implement update
@bottles_api.route(BOTTLE_ROUTES['update'].path, methods=BOTTLE_ROUTES['update'].methods)
def update_bottle(bottle_id: str):
    """
    Update a bottle from the database by id
    """
    data = request.json

    bottle = bottleFromRequest(data=data)

    res = bottles_col.document(bottle_id).set(bottle.to_json())
    print(str(res))

    return bottle.to_json()


# Todo: Implement delete
@bottles_api.route(BOTTLE_ROUTES['delete'].path, methods=BOTTLE_ROUTES['delete'].methods)
def delete_bottle(bottle_id: str):
    """
    Delete a bottle from the database by id
    """
    bottles_col.document(bottle_id).delete()
    print("Bottle deleted")

    return "Bottle deleted"
