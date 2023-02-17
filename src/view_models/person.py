from flask_restx import fields


from src.resources import api
from src.view_models.simple_family import simple_family_model

person_model = api.model(
    "Person",
    {
        "id": fields.Integer,
        "name": fields.String,
        "family_id": fields.Integer,
        "family": fields.Nested(simple_family_model),
        "gender": fields.Integer,
        "manage_families": fields.Nested(simple_family_model),
    },
)
