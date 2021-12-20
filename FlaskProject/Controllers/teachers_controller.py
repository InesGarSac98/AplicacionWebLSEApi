from flask import jsonify, Blueprint, request, make_response
import json

# imports for PyJWT authentication

teachers_controller = Blueprint("teachers_controller", __name__, static_folder="Controllers")

from .Models.teacher import Teacher
from app import db

# User Database Route
# this route sends back list of users users
@teachers_controller.route('/', methods=['GET'])
# @token_required
# def get_all_users(current_user):
def get_all_teachers():
	# querying the database
	# for all the entries in it
	teachers = Teacher.query.all()
	# converting the query objects
	# to list of jsons
	output = []
	for teacher in teachers:
		# appending the user data json
		# to the response list
		output.append({
			'userId': teacher.userId,
			'schoolName': teacher.schoolName
		})

	return jsonify(output)


@teachers_controller.route('/', methods=['POST'])
@teachers_controller.route('', methods=['POST'])
# @token_required
def create_teacher():
	new_teacher = request.get_json()
	data = dict(new_teacher)
	teacher = Teacher(**data)
	db.session.add(teacher)
	db.session.commit()
	return make_response(teacher.serialize())
