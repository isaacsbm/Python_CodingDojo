from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe():
    db = "recipes"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data.get("instruction")
        self.under_30_min = data["under_30_min"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = data["user_name"]
        self.recipe = []

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT recipes.id, recipes.name, recipes.description, recipes.under_30_min, recipes.created_at, recipes.updated_at, users.first_name as user_name FROM recipes JOIN users ON recipes.users_id = users_id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe.user_name = row['user_name']
            recipes.append(recipe)
        return recipes
    @classmethod # ! There has to be an easier way to write this?? What is that? Because this is messing up the rest of my code...Look at instructions I had to put it as a get not a data????
    def get_one_recipe(cls,data):
        query = "SELECT recipes.id, recipes.name, recipes.description, recipes.instruction,recipes.under_30_min, recipes.created_at, recipes.updated_at, users.first_name as user_name FROM recipes JOIN users ON recipes.users_id = users_id WHERE recipes.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])
    @classmethod
    def create_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, instruction, under_30_min, created_at) VALUES (%(name)s,%(des)s,%(inst)s,%(u3)s,%(ct)s)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results