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

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("login_and_registration").query_db(query, data)
        all_users = []
        for row in results:
            one_user = cls(row)
            # all_users.append(one_user)
        return one_user

    @classmethod
    def get_id_from_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL("login_and_registration").query_db(query, data)
        all_users = []
        for row in results:
            # pass
            one_user = cls(row)
            all_users.append(one_user)
        # all_users = cls(results)
        user_id = all_users[0].id
        return user_id

    @staticmethod
    def validate_register(reg_info):
        is_valid = True

        # Is submitted

        # Length checks
        if len(reg_info["r_first_name"]) < 2:
            flash("First Name must be at least 2 characters.","register")
            is_valid = False
        if len(reg_info["r_last_name"]) < 2:
            flash("Last Name must be at least 2 characters.","register")
            is_valid = False
        if len(reg_info["r_email"]) < 2:
            flash("Email must be at least 2 characters.","register")
            is_valid = False
        if len(reg_info["r_password"]) < 2:
            flash("Password must be at least 2 characters.","register")
            is_valid = False
        if len(reg_info["r_confirm_password"]) < 2:
            flash("Password must be at least 2 characters.","register")
            is_valid = False

        # Check Email Stuff
        snail = "@"
        dot = "."
        if not snail in reg_info["r_email"]:
            flash("@ must be in Email.","register")
            is_valid = False
        if not dot in reg_info["r_email"]:
            flash(". must be in Email.","register")
            is_valid = False
        
        # Check Matching Passwords
        if not reg_info["r_confirm_password"] == reg_info["r_password"]:
            flash("Passwords must match.","register")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(log_info):
        is_valid = True

                # Length checks
        if len(log_info["l_email"]) < 2:
            flash("Email must be at least 2 characters.","login")
            is_valid = False
        if len(log_info["l_password"]) < 2:
            flash("Password must be at least 2 characters.","login")
            is_valid = False

        return is_valid