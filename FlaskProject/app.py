# flask imports
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

app.config['SECRET_KEY'] = 'z_u?UN7pNcs9xW$rheYqnpxhn_&8j5uy'

dbConnectionString = 'sqlite:///DB/Database.db'
if len(sys.argv) > 1:
    dbConnectionString = 'sqlite:///DB/' + sys.argv[1] + '.db'
app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectionString

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
config = app.config
db = SQLAlchemy(app)

from Controllers.users_controller import users_controller
from Controllers.teachers_controller import teachers_controller
from Controllers.students_controller import students_controller
from Controllers.classrooms_controller import classrooms_controller
from Controllers.words_controller import words_controller
from Controllers.games_controller import games_controller
from Controllers.classroomsGames_controller import classroomGames_controller
from Controllers.classroomsWords_controller import classroomWords_controller
from Controllers.gameEvent_controller import gameEvent_controller
from Controllers.quizzGameQuestions_controller import quizzGameQuestions_controller
from Controllers.quizzGameAnswers_controller import quizzGameAnswers_controller
from Controllers.statistics_controller import statistics_controller
from Controllers.quizzGameClassroomConfiguration_controller import quizzGameClassroomConfiguration_controller
from Controllers.memoryGameClassroomConfiguration_controller import memoryGameClassroomConfiguration_controller
from Controllers.student_learned_words_controller import student_learned_words_controller

app.register_blueprint(users_controller, url_prefix="/api/users")
app.register_blueprint(teachers_controller, url_prefix="/api/teachers")
app.register_blueprint(students_controller, url_prefix="/api/students")
app.register_blueprint(classrooms_controller, url_prefix="/api/classrooms")
app.register_blueprint(words_controller, url_prefix="/api/words")
app.register_blueprint(games_controller, url_prefix="/api/games")
app.register_blueprint(classroomGames_controller, url_prefix="/api/classroomGames")
app.register_blueprint(classroomWords_controller, url_prefix="/api/classroomWords")
app.register_blueprint(gameEvent_controller, url_prefix="/api/gameEvents")
app.register_blueprint(quizzGameQuestions_controller, url_prefix="/api/quizzGameQuestions")
app.register_blueprint(quizzGameAnswers_controller, url_prefix="/api/quizzGameAnswers")
app.register_blueprint(statistics_controller, url_prefix="/api/statistics")
app.register_blueprint(quizzGameClassroomConfiguration_controller, url_prefix="/api/quizzGameClassroomConfiguration")
app.register_blueprint(memoryGameClassroomConfiguration_controller, url_prefix="/api/memoryGameClassroomConfiguration")
app.register_blueprint(student_learned_words_controller, url_prefix="/api/studentLearnedWords")

if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debuger shell
    # if you hit an error while running the server
    app.run(port=3000, debug=True)
