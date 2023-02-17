from flask_restx import fields


from src.resources import api

simple_person_model = api.model(
    "SimplePerson",
    {
        "id": fields.Integer,
        "name": fields.String,
        "gender": fields.Integer,
        "family_id": fields.Integer,
    },
)
