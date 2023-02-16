import json

from sqlalchemy import func
from flask_restx import fields


from project import api
from project.config.databases import db
from project.config.datetime_encoder import DatetimeEncoder
from project.config.hashs import Hash


class Family(db.Model):  # type: ignore
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    chief_person_id = db.Column(db.Integer, nullable=False)
    join_family_id = db.Column(db.Integer, nullable=True)
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


family_model = api.model(
    "Family",
    {
        "id": fields.Integer,
        "name": fields.String,
        "chief_person_id": fields.Integer,
        "join_family_id": fields.Integer,
    },
)
