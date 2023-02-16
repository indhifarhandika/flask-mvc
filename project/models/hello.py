import json

"""
    Import local package
"""
from project.config.database import db
from project.config.datetime_encoder import DatetimeEncoder
from project.config.hash import Hash


class Hello:
    def __init__(self):
        pass

    def first_greeting(self):
        return {"title": "Hello World", "body": "Flask simple MVC"}
