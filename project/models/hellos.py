import json

"""
    Import local package
"""
from project.config.databases import db
from project.config.datetime_encoder import DatetimeEncoder
from project.config.hashs import Hash


class Hello:
    def __init__(self):
        pass

    def first_greeting(self):
        return {"title": "Hello World", "body": "Flask simple MVC"}
