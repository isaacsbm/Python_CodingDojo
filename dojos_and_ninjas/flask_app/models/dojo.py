from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo():
    def __init__(self, data) -> None:
        self.id = ["id"]
        self.name=["name"]
        self.created_at["created_at"]
        self.updated_at["updated_at"]
    