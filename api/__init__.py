from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("config/key.json")
default_app = initialize_app(cred)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234rtfescdvf'

    from .bottles_api import bottles_api

    app.register_blueprint(bottles_api, url_prefix='/bottles')

    return app


print("Done")
