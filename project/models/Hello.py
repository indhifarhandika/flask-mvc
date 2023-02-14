import json

"""
    Import local package
"""
from project.config.Database import connection as con, cursor as cur
from project.config.DatetimeEncoder import DatetimeEncoder
from project.config.Hash import Hash

"""
    Your Code
"""


class Hello:
    def __init__(self):
        pass

    def first_greeting(self):
        return {"title": "Hello World", "body": "Flask simple MVC"}
