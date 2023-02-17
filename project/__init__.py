import logging
from flask import Flask
from flask_restx import Api

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/genealogy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

from project.controllers.api import *
