from flask_restx import fields


from src import api, db
from src.models.mixin import Mixin


class Person(Mixin, db.Model):  # type: ignore
    name = db.Column(db.String(255), nullable=False, use_existing_column=True)
    family_id = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.Integer, nullable=False)
    join_person_id = db.Column(db.Integer, nullable=True)

    def __init__(self, name, family_id, gender):
        super().__init__()
        self.name = name
        self.family_id = family_id
        self.gender = gender

    def __repr__(self):
        return f"<Person {self.name}>"


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
