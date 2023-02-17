from flask_restx import fields


from src import api, db
from src.models.mixin import Mixin


class Family(Mixin, db.Model):  # type: ignore
    name = db.Column(db.String(255), nullable=False)
    chief_person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=True)
    chief_person = db.relationship(
        "Person",
        foreign_keys=[chief_person_id],
        backref="manage_families",
        lazy=True,
    )

    simple_person_model = api.model(
        "SimplePerson",
        {
            "id": fields.Integer,
            "name": fields.String,
            "gender": fields.Integer,
        },
    )

    model = api.model(
        "Family",
        {
            "id": fields.Integer,
            "name": fields.String,
            "chief_person_id": fields.Integer,
            "chief_person": fields.Nested(simple_person_model),
            "persons": fields.Nested(simple_person_model),
        },
    )

    def __init__(self, name, chief_person_id):
        super().__init__()
        self.name = name
        # self.chief_person_id = chief_person_id

    def __repr__(self):
        return f"<Family {self.name}>"
