# flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'z_u?UN7pNcs9xW$rheYqnpxhn_&8j5uy'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
config = app.config
db = SQLAlchemy(app)

from Controllers.users_controller import users_controller
from Controllers.teachers_controller import teachers_controller
from Controllers.students_controller import students_controller
#from Controllers.studentAvailableGame_controller import studentAvailableGame_controller
from Controllers.words_controller import words_controller

app.register_blueprint(users_controller, url_prefix="/api/users")
app.register_blueprint(teachers_controller, url_prefix="/api/teachers")
app.register_blueprint(students_controller, url_prefix="/api/students")
#app.register_blueprint(studentAvailableGame_controller, url_prefix="/api/studentsAvailableGame")
app.register_blueprint(words_controller, url_prefix="/api/words")

if __name__ == "__main__":
	# setting debug to True enables hot reload
	# and also provides a debuger shell
	# if you hit an error while running the server
	app.run(port = 3000, debug = True)
