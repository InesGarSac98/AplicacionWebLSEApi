from flask import Blueprint, request, make_response
from .Models.classroomWords import ClassroomWords
from .Services.token_services import allow_only_teachers

classroomWords_controller = Blueprint("classroomWords_controller", __name__, static_folder="Controllers")

from app import db


@classroomWords_controller.route('/', methods=['POST'])
@classroomWords_controller.route('', methods=['POST'])
@allow_only_teachers
def create_classroomWord():
	new_classroomWord = request.get_json()
	data = dict(new_classroomWord)
	classroomWord = ClassroomWords(**data)
	db.session.execute('PRAGMA foreign_keys = ON;')
	db.session.add(classroomWord)
	db.session.commit()
	return make_response(classroomWord.serialize())


@classroomWords_controller.route('/<int:id>', methods=['DELETE'])
@classroomWords_controller.route('<int:id>', methods=['DELETE'])
@allow_only_teachers
def delete_classroomWord(id):
	db.session.execute('PRAGMA foreign_keys = ON;')
	ClassroomWords.query.filter(ClassroomWords.id == id).delete()
	db.session.commit()
	return make_response()


