# flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager, UserMixin, login_user


# creates Flask object
app = Flask(__name__)
# configuration
# NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# INSTEAD CREATE A .env FILE AND STORE IN IT
app.config['SECRET_KEY'] = 'your secret key'
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
db = SQLAlchemy(app)

import Models.user

from Controllers.prueba import *


if __name__ == "__main__":
	# setting debug to True enables hot reload
	# and also provides a debuger shell
	# if you hit an error while running the server
	app.run(port = 3000, debug = True)
