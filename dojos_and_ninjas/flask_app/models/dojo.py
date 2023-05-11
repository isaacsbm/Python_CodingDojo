from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo():
    db = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            # new_dojo= cls(dojo)
            dojos.append(cls(dojo))
        return dojos
    
    # @classmethod
    # def get_dojo_with_ninjas(cls,data):
    #     query = """
    #         SELECT *
    #         FROM dojos
    #         LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
    #         WHERE dojos.id = %(id)s;
    #     """
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     print("--------------------------")
    #     print(results)
    #     dojo = cls(results[0])
    #     for row in results:
    #         ninja_data = {
    #             "id": row["id"],
    #             "first_name": row["first_name"],
    #             "last_name": row["last_name"],
    #             "age": row["age"],
    #             "created_at": row["created_at"],
    #             "updated_at": row["updated_at"],
    #             "dojo_id": row["dojo_id"]
    #         }
    #         # d = cls(row)
    #         dojo.ninjas.append(ninja.Ninja(ninja_data))
    #         # ninja_data.append(d)
    #     return dojo

    @classmethod
    def get_dojo_with_ninjas(cls,data):
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
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "dojo_id": row["dojo_id"]
            }
            # d = cls(row)
            dojo.ninjas.append(ninja.Ninja(ninja_data))
            # ninja_data.append(d)
        return dojo
