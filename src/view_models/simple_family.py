from flask_restx import fields


from src.resources import api

simple_family_model = api.model(
    "SimpleFamily",
    {
        "id": fields.Integer,
        "name": fields.String,
        "chief_person_id": fields.Integer,
    },
)
