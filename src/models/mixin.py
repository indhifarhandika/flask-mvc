from sqlalchemy import func


from src.models import db


class Mixin(object):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
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

    session = db.session
