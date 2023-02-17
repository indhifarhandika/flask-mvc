from src import db
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

    def __init__(self, name, chief_person_id):
        super().__init__()
        self.name = name
        # self.chief_person_id = chief_person_id

    def __repr__(self):
        return f"<Family {self.name}>"
