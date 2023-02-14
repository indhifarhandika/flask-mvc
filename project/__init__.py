from flask import Flask

app = Flask("project")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/genealogy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from project.controllers import *
