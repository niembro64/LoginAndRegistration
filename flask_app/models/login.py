from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Login:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.password = data["password"]
        self.email = data["email"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, password, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(password)s, %(email)s, NOW(), NOW());"
        new_id = connectToMySQL("login_and_registration").query_db(query, data)
        return new_id

    @staticmethod
    def validate_login(login):
        is_valid = True

        # Length checks
        if len(login["r_first_name"]) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(login["r_last_name"]) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
        if len(login["r_email"]) < 2:
            flash("Email must be at least 2 characters.")
            is_valid = False
        if len(login["r_password"]) < 2:
            flash("Password must be at least 2 characters.")
            is_valid = False
        if len(login["r_confirm_password"]) < 2:
            flash("Password must be at least 2 characters.")
            is_valid = False

        # Check Email Stuff
        snail = "@"
        dot = "."
        if not snail in login["r_email"]:
            flash("@ must be in Email.")
            is_valid = False
        if not dot in login["r_email"]:
            flash(". must be in Email.")
            is_valid = False
        
        # Check Matching Passwords
        if not login["r_confirm_password"] == login["r_password"]:
            flash("Passwords must match.")
            is_valid = False

        return is_valid
