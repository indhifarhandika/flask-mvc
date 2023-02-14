import json

"""
    Import local package
"""
from project.config.Database import db
from project.config.DatetimeEncoder import DatetimeEncoder
from project.config.Hash import Hash


class Hello:
    def __init__(self):
        pass

    def first_greeting(self):
        return {"title": "Hello World", "body": "Flask simple MVC"}
