import os, glob


__all__ = [
    os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")
]


def create_app():
    import logging
    from flask import Flask
    from src.models import db
    from src.resources import api, add_resources

    logging.basicConfig(level=logging.INFO)

    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://root:root@localhost/genealogy"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    api.init_app(app)
    add_resources()

    return app
