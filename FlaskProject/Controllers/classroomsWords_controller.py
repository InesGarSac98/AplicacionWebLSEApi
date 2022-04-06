from flask import jsonify, Blueprint, request, make_response
import json

from .Models.classroomWords import ClassroomWords

classroomWords_controller = Blueprint("classroomWords_controller", __name__, static_folder="Controllers")

from app import db


@classroomWords_controller.route('/', methods=['POST'])
@classroomWords_controller.route('', methods=['POST'])
# @token_required
def create_classroomWord():
	new_classroomWord = request.get_json()
	data = dict(new_classroomWord)
	classroomWord = ClassroomWords(**data)
	db.session.add(classroomWord)
	db.session.commit()
	return make_response(classroomWord.serialize())


@classroomWords_controller.route('/<int:id>', methods=['DELETE'])
@classroomWords_controller.route('<int:id>', methods=['DELETE'])
# @token_required
def delete_classroomWord(id):
	ClassroomWords.query.filter(ClassroomWords.id == id).delete()
	db.session.commit()
	return make_response()


