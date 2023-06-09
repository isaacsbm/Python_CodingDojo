from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User():
    db = "users"
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            new_user= cls(user)
            users.append(new_user)
        return users
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(fn)s,%(ln)s,%(email)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(query)
        return results

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(email)s WHERE id=%(id)s;"
        results =  connectToMySQL(cls.db).query_db(query,data)
        print("---------------------------------------")
        return results
    
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def is_valid(users):
        is_valid = True
        if len(users['first_name']) < 2:
            is_valid = False
            flash("First Name should have at least 2 characters")
        if len(users['last_name']) < 2:
            is_valid = False
            flash("Last Name should have at least 2 characters")
        if not EMAIL_REGEX.match(users['email']):
            is_valid = False
            flash("Invalid Email address!")
        return is_valid