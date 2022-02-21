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

@app.route("/login_user", methods=["POST"])
def fun_login():

    if not Login.validate_login(request.form):
        return redirect("/")

    data = {
        "email": request.form["l_email"]
    }

    user_id = Login.get_id_from_email(data)

    data = {
        "id": user_id
    }

    one_user = Login.get_user(data)
  
    session['user_id'] = one_user.id
    session['first_name'] = one_user.first_name
    session['last_name'] = one_user.last_name
    session['password'] = one_user.password
    session['email'] = one_user.email

    return redirect(f"/user/{user_id}")



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
