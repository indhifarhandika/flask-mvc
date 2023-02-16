import json

from sqlalchemy import func
from flask_restx import fields


from project import api
from project.config.databases import db
from project.config.datetime_encoder import DatetimeEncoder
from project.config.hashs import Hash


class RelationshipType(db.Model):  # type: ignore
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
    )

    def __repr__(self):
        return f"<Family {self.name}>"


relationship_type_model = api.model(
    "RelationshipType",
    {
        "id": fields.Integer,
        "name": fields.String,
    },
)
