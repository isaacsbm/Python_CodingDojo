from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookies():
    db = "cookie_orders"
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.num_of_boxes = data["num_of_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    # * Get all cookies
    @classmethod
    def get_all_cookies(cls):
        query = "SELECT * FROM cookies"
        results = connectToMySQL(cls.db).query_db(query)
        cookies = []
        for cookie in results:
            cookies.append(cls(cookie))
        return cookies
    # * Get one cookie
    @classmethod
    def get_one_order(cls,data):
        query = "SELECT * FROM cookies WHERE id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])
    # * create order
    @classmethod
    def create_order(cls,data):
        query = "INSERT INTO cookies (name, cookie_type, num_of_boxes) VALUES (%(name)s, %(ct)s,%(nob)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(query)
        print(results)
        return results
    
    # * update order
    @classmethod
    def edit_order(cls,data):
        query = "UPDATE cookies SET name=%(name)s, cookie_type=%(ct)s, num_of_boxes=%(nob)s WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    # * Validation
    @staticmethod
    def is_valid(cookies):
        is_valid = True
        
        if len(cookies["name"]) < 2:
            is_valid = False
            flash("Name must be longer than two characters")
        if len(cookies["cookie_type"]) < 2:
            is_valid = False
            flash("Cookie type must be longer than two characters")
        if len(cookies["num_of_boxes"]) < 0:
            is_valid = False
            flash("Integer must be postive")
        return is_valid