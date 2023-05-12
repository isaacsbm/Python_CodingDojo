from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe():
    db = "recipes"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.under_30_min = data["under_30_min"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = data["users_id"]
        self.user = None

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.users_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipe_dict = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email":row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            recipe_dict.user = user.User(user_data)
            recipes.append(recipe_dict)
        return recipes
    @classmethod # ! There has to be an easier way to write this?? What is that? Because this is messing up the rest of my code...Look at instructions I had to put it as a get not a data????
    def get_one_recipe(cls,data):
        query = "SELECT * FROM recipes JOIN users on recipes.users_id = users.id WHERE recipes.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        results = results[0]
        recipe_one = cls(results)
        for row in results:
            user_data = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
        recipe_one.user = user.User(user_data)
        return recipe_one

    @classmethod
    def create_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, instruction, under_30_min, created_at, users_id) VALUES (%(name)s,%(des)s,%(inst)s,%(u3)s,%(ct)s, %(users_id)s)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results