from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    db = "ninjas"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]
        self.dojo = []
    
    @classmethod
    def create_ninja(cls):
        query = "INSERT INTO ninjas (first_name, last_name, age)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
