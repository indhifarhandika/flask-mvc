import logging
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/genealogy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
db = SQLAlchemy(app)

from src.apis import *
