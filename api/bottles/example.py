from models import Bottle

if __name__ == '__main__':
    bottle = Bottle(_id="https://www.thewhiskyexchange.com/p/3121/lagavulin-16-year-old",
                    name="Lagavulin 16 Year Old",
                    special='None',
                    description="The Islay representative in the 'Classic Malts' series is a deep, dry and exceptionally peaty bruiser. Probably the most pungent of all Islay malts, Lagavulin is not for the faint-hearted but inspires fanatical devotion in its many followers.",
                    abv="43%",
                    price="\u00a381.75",
                    attributes={
                        "category": "Scotch Whisky",
                        "type": "Single Malt Scotch Whisky",
                        "region": "Islay",
                        "distiller": "Lagavulin",
                        "cask": "None"
                    },
                    recommended=[
                        "https://www.thewhiskyexchange.com/p/34537/macallan-12-year-old-double-cask",
                        "https://www.thewhiskyexchange.com/p/114/ardbeg-uigeadail",
                        "https://www.thewhiskyexchange.com/p/552/johnnie-walker-blue-label",
                        "https://www.thewhiskyexchange.com/p/47802/deanston-18-year-old",
                        "https://www.thewhiskyexchange.com/p/51008/glenallachie-15-year-old-sherry-cask",
                        "https://www.thewhiskyexchange.com/p/3512/macallan-12-year-old-sherry-oak",
                        "https://www.thewhiskyexchange.com/p/56202/lagavulin-2003-distillers-edition-bot2019",
                        "https://www.thewhiskyexchange.com/p/66329/lg12-elements-of-islay",
                        "https://www.thewhiskyexchange.com/p/63731/lagavulin-2006-distillers-edition-bot2021",
                        "https://www.thewhiskyexchange.com/p/57767/lagavulin-8-year-old",
                        "https://www.thewhiskyexchange.com/p/56714/lagavulin-10-year-old",
                        "https://www.thewhiskyexchange.com/p/47810/lagavulin-9-year-old-game-of-thrones-house-lannister"
                    ],
                    whiskey_exchange_url="https://www.thewhiskyexchange.com/p/3121/lagavulin-16-year-old",
                    image_url="https://img.thewhiskyexchange.com/900/lgvob.16yo.jpg"
                    )

# ? Create a new bottle
# bottle = Bottle('Example bottle')

# ? Call a method
bottle.greet()
bottle.cost()

# ? Set a bottle property
# bottle.name = 'Another example'

# bottle.greet()
