from flask_app.config.mysqlconnection import connectToMySQL


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


