from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.login import Login

@app.route("/")
def show_index():
    return render_template("index.html")