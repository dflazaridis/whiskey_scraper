import re
import json
from selenium.webdriver.common.by import By
# from api import create_new_whiskey

ALLOWED_CATEGORIES = ["Scotch Whisky", "World Whisky"]


def get_first_bottle_url(driver):
    driver.get('https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky')
    first_product_card = driver.find_elements(By.CLASS_NAME, "product-card")[0]
    url = first_product_card.get_attribute("href").split("?")[0]
    print("Whiskey URL Found:", url)

    return url


# Function that gathers all whiskey URLs on given pages, iterates through them and grabs attributes
def scrape_whiskey_data_url(driver, whiskeys, url, count=300):
    print("Count is: " + str(len(whiskeys.keys())))

    if len(whiskeys.keys()) >= count:
        return whiskeys

    whiskey = get_whiskey_attributes(driver, url)
    category = whiskey['attributes']['category']

    # don't add a bottle to the dictionary if not a whiskey
    if not category in ALLOWED_CATEGORIES:
        print(f'This is not a whiskey, the type is {category}')
        return whiskeys

    whiskeys[url] = whiskey
    # output_whiskey_to_json(whiskeys)

    for url in whiskey["recommended"]:
        if len(whiskeys.keys()) >= count:
            return whiskeys

        if not url in whiskeys:
            whiskeys = scrape_whiskey_data_url(
                driver, whiskeys, url, count=count)

    return whiskeys


def get_whiskey_name(driver):
    try:
        whiskey_name = driver.find_element(
            By.CLASS_NAME, "product-main__name").text

    except Exception:
        return None, None

    whiskey_name = str(whiskey_name)
    whiskey_name = whiskey_name.split("\n")
    name = whiskey_name[0]
    special = None

    for index in range(0, 2):
        try:
            whiskey_name[index]
            special = whiskey_name[1]

        except Exception:
            special = None

    return {"name": name, "special": special}


# returns the type of alcohol
def get_alcohol_category(driver):

    category = None

    try:
        breadcrumbs = driver.find_element(
            By.CLASS_NAME, "breadcrumb__list").text
        category = breadcrumbs.split('\n')[1]
    except Exception:
        return

    return category


def get_whiskey_type(driver):

    breadcrumb_list = driver.find_elements(
        By.CLASS_NAME, "breadcrumb__list")

    attribute_list = []

    try:
        for items in breadcrumb_list:  # iterating through and pulling the attributes that are in the breadcrumb list
            attribute_list.append(items.text)

        attribute_list = str(attribute_list)
        attribute_list = attribute_list.split("\\n")
        whiskey_type = attribute_list[2]

        return whiskey_type

    except Exception:
        whiskey_type = None
        return whiskey_type


def get_whiskey_region(driver):

    breadcrumb_list = driver.find_elements(
        By.CLASS_NAME, "breadcrumb__list")

    attribute_list = []

    try:
        for items in breadcrumb_list:  # iterating through and pulling the attributes that are in the breadcrumb list
            attribute_list.append(items.text)

        attribute_list = str(attribute_list)
        attribute_list = attribute_list.split("\\n")
        whiskey_region = attribute_list[3]

    except Exception:
        whiskey_region = None

    return whiskey_region


def get_whiskey_distiller(driver):

    breadcrumb_list = driver.find_elements(
        By.CLASS_NAME, "breadcrumb__list")

    attribute_list = []

    try:
        for items in breadcrumb_list:  # iterating through and pulling the attributes that are in the breadcrumb list
            attribute_list.append(items.text)

        attribute_list = str(attribute_list)
        attribute_list = attribute_list.split("\\n")
        whiskey_distiller = attribute_list[4]

        return whiskey_distiller

    except Exception:
        whiskey_distiller = None
        return whiskey_distiller


def get_whiskey_cask(driver):
    try:
        product_facts = driver.find_elements(
            By.CLASS_NAME, "product-facts__type")

        for attribute in product_facts:
            if attribute.text == "Cask Type":
                return driver.find_element(
                    By.CLASS_NAME, "product-facts__data").text

    except Exception:
        pass

    try:
        name = get_whiskey_name(driver)

        if not name["special"]:
            return

        [cask] = re.findall('(\w+\s+Cask)', name["special"])

        if not cask:
            return
        else:
            return cask

    except Exception:
        pass


def get_whiskey_abv(driver):
    try:
        # return driver.find_element(
        #     By.CLASS_NAME, "product-main__data").text

        whiskey_abv = driver.find_element(
            By.CLASS_NAME, "product-main__data").text.split("/")

        # return percentage abv only and strip whitespace
        whiskey_abv = whiskey_abv[1].strip()

        return whiskey_abv

    except Exception:
        return None


def get_whiskey_price(driver):
    try:
        return driver.find_element(
            By.CLASS_NAME, "product-action__price").text

    except Exception:
        return None


def get_whiskey_description(driver):
    try:
        whiskey_description = driver.find_element(
            By.CLASS_NAME, "product-main__description").text

        whiskey_description = whiskey_description.split('\n')[0]

        return whiskey_description

    except Exception:
        return None


def get_image_url(driver):
    try:
        image_url = driver.find_element(
            By.CLASS_NAME, "product-main__image").get_attribute('src')

        # image_url = image_url.split('\n')[0]

        return image_url

    except Exception:
        return None


def get_whiskey_attributes(driver, url):
    driver.get(url)

    whiskey = {
        **get_whiskey_name(driver),
        'description': get_whiskey_description(driver),
        'abv': get_whiskey_abv(driver),
        'price': get_whiskey_price(driver),
        'attributes': {
            'category': get_alcohol_category(driver),
            'type': get_whiskey_type(driver),
            'region': get_whiskey_region(driver),
            'distiller': get_whiskey_distiller(driver),
            'cask': get_whiskey_cask(driver)
        },
        'recommended': get_recommended_urls(driver),
        'whiskey_exchange_url': url,
        'image_url': get_image_url(driver)
    }

    return whiskey

    # extract cask and preceding word from special note

# return array of recommended bottle urls that is then stored in  whiskey_attributes dict


def get_recommended_urls(driver):

    recommendation = driver.find_elements(
        By.CLASS_NAME, "product-card")

    recommended_url_list = []

    for url in recommendation:
        recommended_url_list.append(url.get_attribute("href").split("?")[0])

    return recommended_url_list[::-1]


'''Output whiskeys dict to JSON'''


def output_whiskey_to_json(whiskeys):
    with open('single_malts.json', 'w') as f:
        json.dump(whiskeys, f)


'''Read in whiskey to JSON object to python'''


def read_whiskey_json(whiskeys):
    with open('single_malts.json', 'r') as whiskeys_json:

        whiskeys = json.loads(whiskeys_json.read())

        return whiskeys
