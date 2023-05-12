from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

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

    #* Get all recipes with User
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.users_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipe_dict = cls(row)
            recipe_dict.first_name = row["first_name"]
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
    
    #* Get One Recipe Tied to the User
    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes JOIN users on recipes.users_id = users.id WHERE recipes.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(query)
        row = results[0]
        recipe_one = cls(results[0])
        recipe_one.first_name = row["first_name"]
        # for row in results:
        user_data = {
            "id": row["users.id"],
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "email": row["email"],
            "password": row["password"],
            "created_at": row["users.created_at"],
            "updated_at": row["users.updated_at"]
        }
        recipe_one.user = user.User(user_data)
        return recipe_one

    # * Create Recipe
    @classmethod 
    def create_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, instruction, under_30_min, created_at, users_id) VALUES (%(name)s,%(des)s,%(inst)s,%(u3)s,%(ct)s, %(users_id)s)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    # * Update Recipe
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(des)s, instruction=%(inst)s, under_30_min=%(u3)s, updated_at=%(ua)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    # * Delete Recipe
    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        yay= connectToMySQL(cls.db).query_db(query,data)
        return yay
    
    @staticmethod
    def is_valid(recipe_dicts):
        is_valid = True
        if len(recipe_dicts["name"]) < 3:
            flash("Name must be longer than 3 characters")
            is_valid=False
        if len(recipe_dicts["description"]) < 3:
            flash("Description must be longer than 3 characters")
            is_valid=False
        if len(recipe_dicts["instruction"]) < 3:
            flash("Instructions must be longer than 3 characters")
            is_valid=False
        return is_valid