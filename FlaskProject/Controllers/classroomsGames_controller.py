from flask import jsonify, Blueprint, request, make_response
import json

# imports for PyJWT authentication
from .Models.classroomGames import ClassroomGames
from .Models.games import Games

classroomGames_controller = Blueprint("classroomGames_controller", __name__, static_folder="Controllers")

from app import db


@classroomGames_controller.route('/', methods=['POST'])
@classroomGames_controller.route('', methods=['POST'])
# @token_required
def create_classroomGame():
	new_classroomGame = request.get_json()
	data = dict(new_classroomGame)
	classroomGame = ClassroomGames(**data)
	db.session.add(classroomGame)
	db.session.commit()
	return make_response(classroomGame.serialize())


