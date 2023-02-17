from flask_restx import fields


from src import api

simple_family_model = api.model(
    "SimpleFamily",
    {
        "id": fields.Integer,
        "name": fields.String,
    },
)
