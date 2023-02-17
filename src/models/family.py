from flask_restx import fields


from src import api, db
from src.models.mixin import Mixin


class Family(Mixin, db.Model):  # type: ignore
    name = db.Column(db.String(255), nullable=False, use_existing_column=True)
    chief_person_id = db.Column(db.Integer, nullable=False)
    join_family_id = db.Column(db.Integer, nullable=True)

    model = api.model(
        "Family",
        {
            "id": fields.Integer,
            "name": fields.String,
            "chief_person_id": fields.Integer,
            "join_family_id": fields.Integer,
        },
    )

    def __init__(self, name, chief_person_id):
        super().__init__()
        self.name = name
        self.chief_person_id = chief_person_id

    def __repr__(self):
        return f"<Family {self.name}>"
