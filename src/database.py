from flask import Flask
from decouple import config

from src.models import db

DATABASE_URI = f"postgresql://{config('DB_USER', default='admin')}:{config('DB_PASSWD', default='admin')}" \
               f"@{config('DB_HOST', default='localhost')}:5432/workshop_db"

SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEY = False


def flask_config(name):
    flask = Flask(name)
    flask.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    flask.config['JSON_SORT_KEYS'] = JSON_SORT_KEY
    db.init_app(flask)
    return flask


def table_creator(app):
    from src.models import db
    from src.models.user import User
    from src.models.debit import Debit
    with app.app_context():
        db.create_all()
        db.session.commit()

