from whiskey_data import get_first_bottle_url, scrape_whiskey_data_url, read_whiskey_json, output_whiskey_to_json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from api import create_app
from api.bottles_api import bottles_api, create_bottle


def get_driver():
    service = Service(r'/Users/dimi/Documents/Tools/chromedriver')
    options = Options()
    options.headless = False
    return webdriver.Chrome(service=service, options=options)


def main(count=300):

    # get driver as chromedriver
    driver = get_driver()

    whiskeys = {}
    whiskeys = read_whiskey_json(whiskeys)

    first_whiskey_url = get_first_bottle_url(driver)

    whiskeys = scrape_whiskey_data_url(
        driver, whiskeys, first_whiskey_url, count)

    driver.quit()

    output_whiskey_to_json(whiskeys)

    return whiskeys


main(count=10)

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=False)


# TO DO, add a function that passes a single url into the API
