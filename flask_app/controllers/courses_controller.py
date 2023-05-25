from flask_app import app
from flask import render_template, redirect, request, session, flash
# have to import the course model here
from flask_app.models.courses_model import Course


@app.route('/courses')
def get_all_courses():

    if "players_id" not in session:
        return redirect('/')
    # ".get_all_rcourses" has to match classmethod exactly for Course class"
    courses_info = Course.get_all_courses()
    print("=================================> COURSE INFO: ", courses_info)

    return render_template('courses.html', courses_info=courses_info)
# take the courses_info (where stored info) and passing it into the html page to display using jinja to parse it.

# ================================================


@app.route('/courses/<int:course_id>')
def course_in_session(course_id):
    session['chosen_course'] = Course.get_course_by_id(
        {"course_id": course_id})
    print(session['chosen_course'])
    return redirect('/')


#  ONCE game ends MAKE SURE TO CLEAR OUT CHOSEN_SELECTIONS
# session.pop('chosen_course)
# session.pop('chosen_game)
# session.pop('chosen_num_of_players)
