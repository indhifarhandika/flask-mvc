"""
    Example Controllers
"""

from project import app
from flask import render_template, redirect, url_for

"""
    Import MOdels
"""
from project.models.Family import Family


# route index
@app.route("/family", methods=["GET"])
def family():
    data = Family.query.all()
    return render_template("index.html.j2", data=data)
