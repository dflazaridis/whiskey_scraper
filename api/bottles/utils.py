from .models import Bottle


def bottleFromRequest(data: any) -> Bottle:
    return Bottle(data['id'], data['name'], data['special'],
                  data['description'], data['abv'], data['price'], data['attributes'], data['recommended'], data['whiskey_exchange_url'], data['image_url'])
