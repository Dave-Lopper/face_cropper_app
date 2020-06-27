import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from .blueprints import crop_blueprint


load_dotenv(".env")


def create_app():
    # App settings
    app = Flask(__name__)
    app.config["ENV"] = os.getenv("FLASK_ENV", "dev")
    app.secret_key = os.environ["SECRET_KEY"]

    # CORS policy and endpoints registering
    CORS(crop_blueprint)
    app.register_blueprint(crop_blueprint)

    return app
