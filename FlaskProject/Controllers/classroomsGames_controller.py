from flask import Blueprint, request, make_response
from .Models.classroomGames import ClassroomGames
from .Services.token_services import allow_only_teachers

classroomGames_controller = Blueprint("classroomGames_controller", __name__, static_folder="Controllers")
from app import db


@classroomGames_controller.route('/', methods=['POST'])
@classroomGames_controller.route('', methods=['POST'])
@allow_only_teachers
def create_classroomGame():
	new_classroomGame = request.get_json()
	data = dict(new_classroomGame)
	classroomGame = ClassroomGames(**data)
	db.session.execute('PRAGMA foreign_keys = ON;')
	db.session.add(classroomGame)
	db.session.commit()
	return make_response(classroomGame.serialize())


@classroomGames_controller.route('/<int:id>', methods=['DELETE'])
@classroomGames_controller.route('<int:id>', methods=['DELETE'])
@allow_only_teachers
def delete_classroomGame(id):
	db.session.execute('PRAGMA foreign_keys = ON;')
	ClassroomGames.query.filter(ClassroomGames.id == id).delete()
	db.session.commit()
	return make_response()

