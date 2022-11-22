import requests

BASE_API_URL = 'https://review-app-psi.vercel.app/api'
# BASE_API_URL = 'https://whiski.app/api'

ITEMS_URL = '/items'
API_KEY = 'EiHeczVnnGt8OSqUGjld1Am9wVC8lJvg'

# post new whiskeys to API


def create_new_whiskey(whiskey):
    headers = {'Authorization': f'Basic {API_KEY}'}
    try:
        result = requests.post(BASE_API_URL+ITEMS_URL,
                               data=whiskey, headers=headers, verify=False)
        print(result)
        return True

    except Exception as e:
        return False


def get_whiskeys(whiskey):
    headers = {'Authorization': f'Basic {API_KEY}'}

    try:
        result = requests.get(BASE_API_URL+ITEMS_URL,
                              data=whiskey, headers=headers, verify=False)
        return True

    except Exception as e:
        return False


if __name__ == "__main__":
    test_whiskey = {'name': 'Kilchoman Machir Bay', 'special': None, 'type': 'Single Malt Scotch Whisky', 'region': 'Islay', 'distiller': 'Kilchoman', 'cask': None, 'abv': '70cl / 46%', 'price': '£39.95', 'description': "Kilchoman's ongoing Machir Bay is a vatting of whisky matured in first-fill bourbon casks for around six years, married and then finished in oloroso sherry butts before bottling.", 'recommendations': ['https://www.thewhiskyexchange.com/p/39120/kilchoman-sanaig-small-bottle?suggested=true&source=productpage&type=brand&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/39119/kilchoman-machir-bay-small-bottle?suggested=true&source=productpage&type=brand&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/39957/kilchoman-machir-bay-and-sanaig-gift-pack-2x20cl?suggested=true&source=productpage&type=brand&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/32560/kilchoman-sanaig?suggested=true&source=productpage&type=brand&sourceProductId=40227',
                                                                                                                                                                                                                                                                                                                                                                                                                                      'https://www.thewhiskyexchange.com/p/40228/kilchoman-machir-bay-gift-pack-2-tasting-glasses?suggested=true&source=productpage&type=brand&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/64419/kilchoman-uk-small-batch-batch-3?suggested=true&source=productpage&type=brand&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/232/arran-10-year-old?suggested=true&source=productpage&type=recommended&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/43962/port-charlotte-10-year-old?suggested=true&source=productpage&type=recommended&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/54500/ardbeg-wee-beastie-5-year-old?suggested=true&source=productpage&type=recommended&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/66/ardbeg-10-year-old?suggested=true&source=productpage&type=recommended&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/114/ardbeg-uigeadail?suggested=true&source=productpage&type=recommended&sourceProductId=40227', 'https://www.thewhiskyexchange.com/p/1619/caol-ila-12-year-old?suggested=true&source=productpage&type=recommended&sourceProductId=40227']}
    create_new_whiskey(test_whiskey)
