from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.games_info_model import Game_Info
from flask_app.models.games_model import Game
from flask_app.models.courses_model import Course


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/games/wolf')
def wolf():
    return render_template('wolfGame.html')


# ==============================================


# ==============================================
@app.route('/choose_game')
def choose_game():
    courses_info = Course.get_all_courses()
    games_info = Game_Info.get_all_game_info()
    # Populating dropdown options
    print(games_info)
    return render_template('choose_game.html', games_info=games_info, courses_info=courses_info)


# ===============================================
@app.route('/games/<int:game_id>')
def game_in_session(game_id):
    session['chosen_game'] = game_id
    print(session['chosen_game'])
    return redirect('/setup_round')

#  ONCE game ends MAKE SURE TO CLEAR OUT CHOSEN_SELECTIONS
# session.pop('chosen_course)
# session.pop('chosen_game)
# session.pop('chosen_num_of_players)
# ===============================================


@app.route('/setup_round')
def setup_round():
    chosen_game = Game.get_game_by_id(
        {"games_id": session['chosen_game']})
    chosen_course = Course.get_course_by_id(
        {"course_id": session['chosen_course']})
    return render_template('setup_round.html', chosen_course=chosen_course, chosen_game=chosen_game)


# ===============================================

@app.route('/play_game', methods=['POST'])
def play_game():

    # if not Game.validate_game(request.form):
    #     return redirect('')

    game_data = {
        'course': session['chosen_course'],
        'game': session['chosen_game']
        # 'name': session['game_name']
    }

    Game.create_game(game_data)
    return render_template('play_game.html')

# ===============================================


@app.route('/play/<int:id>')
def show_play_game(id):
    return render_template('play_game.html')
