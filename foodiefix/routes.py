from flask import render_template
from foodiefix import app, db
from foodiefix.models import User, Recipe


@app.route("/")
def home():
    return render_template("base.html")
