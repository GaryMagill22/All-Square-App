from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.games_info_model import Game_Info
from flask_app.models.courses_model import Course


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/games/wolf')
def wolf():
    return render_template('wolfGame.html')


@app.route('/create_game')
def create_game():
    courses_info = Course.get_all_courses()
    games_info = Game_Info.get_all_game_info()
    print(games_info)
    return render_template('create_game.html', games_info=games_info, courses_info=courses_info)


@app.route('/create_game/play')
def play_game():
    return render_template('play_game.html')
