from flask import jsonify, Blueprint, request, make_response
import json

# imports for PyJWT authentication
from .Services.token_services import token_required, allow_only_teachers

teachers_controller = Blueprint("teachers_controller", __name__, static_folder="Controllers")

from .Models.teacher import Teacher
from .Models.classroom import Classroom
from app import db


@teachers_controller.route('/', methods=['GET'])
@allow_only_teachers
def get_teacher_by_user_id():
	teacher = Teacher.query.filter(Teacher.userId == request.args.get("userId")).first()

	if not teacher:
		return make_response({'message': 'Teacher not found'}, 404)

	return make_response(teacher.serialize())


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


@teachers_controller.route('/<int:teacher_id>/classrooms', methods=['GET'])
@allow_only_teachers
def get_all_teacher_classrooms(teacher_id):
	classrooms = Classroom.query.filter(Classroom.teacherId == teacher_id).all()

	output = []
	for classroom in classrooms:
		students = []
		for student in classroom.Students:
			students.append({
				'id': student.id,
				'user': {
					'name': student.User.name
				}
			})
		output.append({
			'id': classroom.id,
			'teacherId': classroom.teacherId,
			'name': classroom.name,
			'classroomCode': classroom.classroomCode,
			'students': students
		})

	return jsonify(output)
