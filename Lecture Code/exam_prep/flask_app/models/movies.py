from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Movie:
    db = "exam_prep"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.genre = data["genre"]
        self.release_year = data["release_year"]
        self.description = data["description"]
        self.user_id = data["user_id"] # * Could be used to replace and make better my name???
        self.creator = None
    
    # * Get All
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM movies LEFT JOIN users on users.id = movies.user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_movies = []

        for row in results:
            all_movies.append(cls(row))
        return all_movies
    
    # * Create
    @classmethod
    def create(cls,data):
        query = "INSERT INTO movies (title, genre, release_year,description) VALUES (%(title)s,%(genre)s,%(release_year)s,%(description)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    # * Get One
    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * FROM movies LEFT JOIN users on users.id = movies.users_id WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        row = results[0]
        one_movie = cls(results[0])
        user_data = {
            "id": row["id"],
            "username": row["username"],
            "email": row["email"],
            "password": row["password"],
            "created_at": row["users.created_at"],
            "updated_at": row["users.updated_at"]
        }
        one_movie = user.User(user_data)
        return one_movie
    
    # * Update
    @classmethod
    def update(cls, data):
        query = "UPDATE movies SET title=%(title)s, genre=%(genre)s, release_year=%(release_year)s, description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    # * Delete
    @classmethod
    def destroy(cls,data):
        query="DELETE FROM movies WHERE id=%(id)s;"
        sucess = connectToMySQL(cls.db).query_db(query,data)
        return sucess