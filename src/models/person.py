from src.models.mixin import Mixin, db


class Person(Mixin, db.Model):  # type: ignore
    name = db.Column(db.String(255), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey("family.id"), nullable=True)
    family = db.relationship(
        "Family",
        foreign_keys=[family_id],
        backref="persons",
        lazy=True,
    )
    gender = db.Column(db.Integer, nullable=False)

    def __init__(self, name, family_id, gender):
        super().__init__()
        self.name = name
        self.family_id = family_id
        self.gender = gender

    def __repr__(self):
        return f"<Person {self.name}>"
