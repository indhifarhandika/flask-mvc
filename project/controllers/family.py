"""
    Example Controllers
"""

from project import app
from flask import render_template, redirect, url_for, request

"""
    Import MOdels
"""
from project.models.family import Family, db


@app.route("/family", methods=["GET"])
def get_families():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    pagination = Family.query.order_by(Family.id).paginate(page=page, per_page=per_page)
    print(pagination.items)
    return render_template("family/list.html.j2", data=pagination)


# Not TEST
@app.route("/family", methods=["POST"])
def add_family():
    name = request.form["name"]
    chief_person_id = request.form["chief_person_id"]
    family = Family(name=name, chief_person_id=chief_person_id)
    db.session.add(family)
    db.session.commit()
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    pagination = Family.query.order_by(Family.id).paginate(page=page, per_page=per_page)
    print(pagination.items)
    return render_template("family/list.html.j2", data=pagination)


@app.route("/family/<id>", methods=["GET"])
def get_family(id):
    family = Family.query.get(id)
    print(family)
    return render_template("family/view.html.j2", data=family)


# Not TEST
@app.route("/family/<id>", methods=["PUT"])
def edit_family(id):
    family = Family.query.get(id)
    family.name = request.form["name"]
    family.chief_person_id = request.form["chief_person_id"]
    db.session.commit()
    print(family)
    return render_template("family/edit.html.j2", data=family)


# Not TEST
@app.route("/family/<id>", methods=["DELETE"])
def remove_family(id):
    family = Family.query.get(id)
    db.session.delete(family)
    db.session.commit()
    print(family)
    return render_template("family/list.html.j2", data=family)
