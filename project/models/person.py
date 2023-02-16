import json

from sqlalchemy import func
from flask_restx import fields


from project import api
from project.config.database import db
from project.config.datetime_encoder import DatetimeEncoder
from project.config.hash import Hash


class Person(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    family_id = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.Integer, nullable=False)
    join_person_id = db.Column(db.Integer, nullable=True)
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


person_model = api.model(
    "Person",
    {
        "id": fields.Integer,
        "name": fields.String,
        "family_id": fields.Integer,
        "gender": fields.Integer,
        "join_person_id": fields.Integer,
    },
)
