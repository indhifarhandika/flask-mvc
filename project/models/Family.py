import json

from sqlalchemy import func

"""
    Import local package
"""
from project.config.Database import db
from project.config.DatetimeEncoder import DatetimeEncoder
from project.config.Hash import Hash


class Family(db.Model):
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
