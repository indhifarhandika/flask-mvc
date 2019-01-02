from flask import Flask

app = Flask("project")

from project.controllers import *
