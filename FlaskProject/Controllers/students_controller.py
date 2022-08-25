from flask import jsonify, Blueprint, request, make_response

from .Models.student import Student
from .Models.classroom import Classroom
from .Services.token_services import token_required_get_user_id, token_required

students_controller = Blueprint("students_controller", __name__, static_folder="Controllers")

from app import db


@students_controller.route('/<int:student_id>', methods=['GET'])
@students_controller.route('/<int:student_id>/', methods=['GET'])
@token_required
def get_student_by_id(student_id):
	student = Student.query.filter(Student.id == student_id).first()

	if not student:
		return make_response({'message': 'No students found'}, 404)

	return jsonify(student.serialize())


@students_controller.route('/', methods=['POST'])
@students_controller.route('', methods=['POST'])
# @token_required(allowedRole="Student")
def create_student():
	new_student = request.get_json()
	data = dict(new_student)
	db.session.execute('PRAGMA foreign_keys = ON;')
	classroom = Classroom.query.filter(Classroom.classroomCode == data['classroomCode']).first()

	if not classroom:
		return make_response({'message': 'Invalid classroomCode'}, 400)

	student = Student(userId=data['userId'], classroomId=classroom.id)

	db.session.add(student)
	db.session.commit()
	return make_response(student.serialize())


@students_controller.route('/student-loged', methods=['GET'])
@students_controller.route('/student-loged/', methods=['GET'])
@token_required_get_user_id
def get_student_logged(current_user_id):
	student = Student.query.filter(Student.userId == current_user_id).first()

	if not student:
		return make_response({'message': 'No students found'}, 404)

	return jsonify(student.serialize())
