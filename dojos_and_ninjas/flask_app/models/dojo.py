from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():
    def __init__(self, data):
        db = "dojos"
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            new_dojo= cls(dojo)
            dojos.append(new_dojo)
        return dojos
