import os

from dotenv import load_dotenv
from flask import Flask

from .blueprints import crop_blueprint


load_dotenv(".env")


def create_app():
    app = Flask(__name__)
    app.config["ENV"] = os.getenv("FLASK_ENV", "dev")
    app.secret_key = os.environ["SECRET_KEY"]
    app.register_blueprint(crop_blueprint)
    return app
