from flask_app import app
from flask import render_template, request, redirect, flash, session

from flask_app.models.login import Login

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)   

@app.route("/")
def show_index():
    return render_template("index.html")

@app.route("/user/<int:user_id>")
def show_user(user_id):
    return render_template("show_user.html")

#################

@app.route("/register_user", methods=["POST"])
def fun_register():

    if not Login.validate_register(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['r_password'])

    data = {
        "first_name": request.form["r_first_name"],
        "last_name": request.form["r_last_name"],
        "password": pw_hash,
        "email": request.form["r_email"]
    }

    user_id = Login.save_user(data)
    session['user_id'] = user_id

    session['first_name'] = data["first_name"]
    session['last_name'] = data["last_name"]
    session['password'] = data["password"]
    session['email'] = data["email"]

    return redirect(f"/user/{user_id}")
