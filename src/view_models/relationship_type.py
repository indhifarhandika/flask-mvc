from flask_restx import fields


from src.resources import api

relationship_type_model = api.model(
    "RelationshipType",
    {
        "id": fields.Integer,
        "name": fields.String,
    },
)
