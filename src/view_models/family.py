from flask_restx import fields


from src.resources import api
from src.view_models.simple_person import simple_person_model

family_model = api.model(
    "Family",
    {
        "id": fields.Integer,
        "name": fields.String,
        "chief_person_id": fields.Integer,
        "chief_person": fields.Nested(simple_person_model),
        "persons": fields.Nested(simple_person_model),
    },
)
