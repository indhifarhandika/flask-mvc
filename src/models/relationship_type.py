from src.models.mixin import Mixin, db


class RelationshipType(Mixin, db.Model):  # type: ignore
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"<RelationshipType {self.name}>"
