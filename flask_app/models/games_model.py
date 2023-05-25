import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# MODEL USED TO STORE CURRENT GAME SESSION


class Game:
    DB = "all_square_schema_updated"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.min_players = data['min_players']
        self.max_players = data['max_players']
        self.description = data['description']
        self.course_id = data['course_id']
        self.games_info_id = data['games_info_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_games(cls):
        query = """
        SELECT * FROM games_info 
        """
        result = connectToMySQL(cls.DB).query_db(query)

        all_games = []

        for row in result:
            all_games.append(Game(row))
        print("=================================> COURSES FROM DB: ", all_games)
        return all_games


# =========================================


    @classmethod
    def get_game_by_id(cls, data):
        query = """
        SELECT * FROM games
        WHERE id = %(games_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
