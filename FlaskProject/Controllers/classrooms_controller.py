from flask import jsonify, Blueprint, request, make_response
import random
import string
import json

# imports for PyJWT authentication
from .Models.classroom import Classroom
from .Services.token_services import allow_only_teachers, token_required

classrooms_controller = Blueprint("classrooms_controller", __name__, static_folder="Controllers")

from .Models.teacher import Teacher
from app import db


# User Database Route
# this route sends back list of users users
@classrooms_controller.route('/', methods=['GET'])
@allow_only_teachers
def get_all_classrooms():
	classrooms = Classroom.query.all()
	output = []
	for classroom in classrooms:
		output.append({
			'teacherId': classroom.teacherId,
			'name': classroom.name,
			'classroomCode': classroom.clasroomCode
		})

	return jsonify(output)


@classrooms_controller.route('/<id>/', methods=['GET'])
@classrooms_controller.route('/<id>', methods=['GET'])
@token_required
def get_classroom(id):
	classroom = Classroom.query.filter(Classroom.id == id).first()

	return jsonify({
		'id': classroom.id,
		'teacherId': classroom.teacherId,
		'name': classroom.name
	})



@classrooms_controller.route('/', methods=['POST'])
@classrooms_controller.route('', methods=['POST'])
@allow_only_teachers
def create_classroom():
	new_classroom = request.get_json()
	data = dict(new_classroom)
	classroom = Classroom(**data)
	classroom.classroomCode = generate_new_unique_classroom_code()
	db.session.add(classroom)
	db.session.commit()
	return make_response(classroom.serialize())


def generate_new_unique_classroom_code():
	characters = string.ascii_letters +\
		string.digits +\
		string.punctuation +\
		string.ascii_lowercase +\
		string.ascii_uppercase
	code = ''.join(random.choice(characters) for i in range(10))

	return code


@classrooms_controller.route('/<classroom_id>/students', methods=['GET'])
@allow_only_teachers
def get_all_classroom_students(classroom_id):
	classroom = Classroom.query.filter(Classroom.id == classroom_id).first()

	output = []
	for student in classroom.Students:
		output.append({
			'id': student.id,
			'user': {
				'name': student.User.name
			}
		})

	return jsonify(output)


@classrooms_controller.route('/<classroom_id>/words', methods=['GET'])
@token_required
def get_all_classroom_words(classroom_id):
	classroom = Classroom.query.filter(Classroom.id == classroom_id).first()

	output = []
	for classroomWord in classroom.ClassroomWords:
		output.append({
			'id': classroomWord.id,
			'wordId': classroomWord.wordId,
			'word': {
				'id': classroomWord.Word.id,
				'name': classroomWord.Word.name,
				'image': classroomWord.Word.image,
				'video': classroomWord.Word.video,
				'videoDefinition': classroomWord.Word.videoDefinition,
			},
			'classroomId': classroomWord.classroomId
		})

	return jsonify(output)


@classrooms_controller.route('/<classroom_id>/games', methods=['GET'])
@token_required
def get_all_classroom_games(classroom_id):
	classroom = Classroom.query.filter(Classroom.id == classroom_id).first()

	output = []
	for classroomGame in classroom.ClassroomGames:
		output.append({
			'id': classroomGame.id,
			'gameId': classroomGame.gameId,
			'game': {
				'id': classroomGame.Game.id,
				'name': classroomGame.Game.name,
				'image': classroomGame.Game.image
			},
			'classroomId': classroomGame.classroomId
		})

	return jsonify(output)

