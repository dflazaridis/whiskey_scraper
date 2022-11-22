from whiskey_data import get_first_bottle_url, scrape_whiskey_data_url, read_whiskey_json, output_whiskey_to_json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from api import create_app


def get_driver():
    service = Service(r'/Users/dimi/Documents/Tools/chromedriver')
    options = Options()
    options.headless = False
    return webdriver.Chrome(service=service, options=options)


def main(count=10):

    # get driver as chromedriver
    driver = get_driver()

    whiskeys = {}
    whiskeys = read_whiskey_json(whiskeys)

    first_whiskey_url = get_first_bottle_url(driver)
    # first_whiskey_url = '' #comment out above and insert url here if testing for single bottle

    whiskeys = scrape_whiskey_data_url(
        driver, whiskeys, first_whiskey_url, count)

    create_whiskey(whiskeys)

    driver.quit()

    output_whiskey_to_json(whiskeys)

    return whiskeys


main(count=20)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# TO DO, add a function that passes a single url into the API
