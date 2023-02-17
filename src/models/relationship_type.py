from flask_restx import fields


from src import api, db
from src.models.mixin import Mixin


class RelationshipType(Mixin, db.Model):  # type: ignore
    name = db.Column(db.String(255), nullable=False, use_existing_column=True)

    model = api.model(
        "RelationshipType",
        {
            "id": fields.Integer,
            "name": fields.String,
        },
    )

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"<RelationshipType {self.name}>"
