from flask_app.config.mysqlconnection import connectToMySQL
class Resume():
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.languages = data["languages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def create(cls,data):
        query = "INSERT INTO resumes (name, age, languages) VALUES (%(name)s, %(age)s,%(languages)s);"
        return connectToMySQL("resume").query_db(query,data)
    
    @classmethod
    def get(cls,data):
        query = "SELECT * FROM resumes WHERE id = %(id)s"
        return cls(connectToMySQL("resumes").query_db(query,data)[0])