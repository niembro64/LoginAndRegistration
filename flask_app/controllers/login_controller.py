from flask_app import app
from flask import render_template, request, redirect, flash

from flask_app.models.login import Login


@app.route("/")
def show_index():
    return render_template("index.html")


@app.route("/user/<int:user_id>")
def show_user(user_id):
    return render_template("show_user.html")

#################


@app.route("/register_user", methods=["POST"])
def fun_register():

    if not Login.validate_login(request.form):
        return redirect("/")

    data = {
        "first_name": request.form["r_first_name"],
        "last_name": request.form["r_last_name"],
        "password": request.form["r_password"],
        "email": request.form["r_email"]
    }
    user_id = Login.save_user(data)
    return redirect("/user/3")
