from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja():
    db = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]
        self.ninjas = []
    
    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def get_ninja_with_dojo(cls,data):
        query = """
            SELECT *
            FROM dojos
            LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        print("--------------------------")
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "dojo_id": row["dojo_id"]
            }
            # d = cls(row)
            dojo.ninjas.append(Ninja(ninja_data))
            # ninja_data.append(d)
        return dojo
    @classmethod
    def update_user(cls,data):
        query = "UPDATE dojos_and_ninjas.ninjas SET first_name=%(fn)s, last_name=%(ln)s, age=%(age)s WHERE ninjas.id=%(id)s;"
        results =  connectToMySQL(cls.db).query_db(query,data)
        print(query)
        print("---------------------------------------")
        print(results)
        return results
    # @classmethod
    # def get_one_by_id(cls, data):
    #     data = {
    #                 "id": id,
    #             }
    #     query = "SELECT * FROM dojos_and_ninjas.ninjas where id=%(id)s"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     return cls(results[0])