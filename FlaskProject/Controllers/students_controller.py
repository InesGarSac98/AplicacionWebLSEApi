from flask import jsonify, Blueprint, request, make_response
import json

# imports for PyJWT authentication
from .Models.student import Student
from .Models.classroom import Classroom

students_controller = Blueprint("students_controller", __name__, static_folder="Controllers")

from .Models.teacher import Teacher
from app import db

# User Database Route
# this route sends back list of users users
@students_controller.route('/', methods=['GET'])
# @token_required
# def get_all_users(current_user):
def get_all_students():
	# querying the database
	# for all the entries in it
	students = Student.query.all()
	# converting the query objects
	# to list of jsons
	output = []
	for student in students:
		# appending the user data json
		# to the response list
		output.append({
			'userId': student.userId,
			'classroomId': student.classroomId
		})

	return jsonify(output)


@students_controller.route('/', methods=['POST'])
@students_controller.route('', methods=['POST'])
# @token_required(allowedRole="Student")
def create_student():
	new_student = request.get_json()
	data = dict(new_student)

	classroom = Classroom.query.filter(Classroom.classroomCode == data['classroomCode']).first()

	if not classroom:
		return make_response({'message': 'Invalid classroomCode'}, 400)

	student = Student(userId=data['userId'], classroomId=classroom.id)

	db.session.add(student)
	db.session.commit()
	return make_response(student.serialize())
