"""
    Example Controllers
"""

from project import app
from flask import render_template, redirect, url_for

"""
    Import MOdels
"""
from project.models.hellos import Hello


# route index
@app.route("/hello", methods=["GET"])
def hello():
    data = Hello().first_greeting()
    return render_template("index.html.j2", data=data)
