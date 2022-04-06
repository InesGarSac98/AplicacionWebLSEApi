from flask import jsonify, Blueprint, request, make_response
import random
import string
import json

# imports for PyJWT authentication
from sqlalchemy import text

from .Models.classroom import Classroom
from .Services.token_services import allow_only_teachers, token_required

statistics_controller = Blueprint("statistics_controller", __name__, static_folder="Controllers")

from .Models.teacher import Teacher
from app import db


# User Database Route
# this route sends back list of users users
@statistics_controller.route('/', methods=['GET'])
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


@statistics_controller.route('/student/<int:studentid>/', methods=['GET'])
@statistics_controller.route('/student/<int:studentid>', methods=['GET'])
@token_required
def get_student_statistics(studentid):
	sql = text('''
		SELECT
			(
				(SELECT leftTime FROM GameEvents g2
					WHERE studentId = :studentid AND status = 0 AND g1.gameplayId = g2.gameplayId)
				-
				(SELECT leftTime FROM GameEvents g2
					WHERE studentId = :studentid AND status IN (2, 3, 4) AND g1.gameplayId = g2.gameplayId)
			) as duration,
			g1.date,
			g1.status,
			g1.score
			FROM GameEvents g1 WHERE studentId = :studentid AND status IN (2, 3, 4)
	''')
	result = db.engine.execute(sql, {'studentid': studentid})

	statisticsResult = []
	for row in result:
		statisticsResult.append({
			'duration': row[0],
			'date': row[1],
			'status': row[2],
			'score': row[3]
		})

	return jsonify(statisticsResult)


@statistics_controller.route('/classroom/<int:classroomid>/', methods=['GET'])
@statistics_controller.route('/classroom/<int:classroomid>', methods=['GET'])
@token_required
def get_classroom_statistics(classroomid):
	sql2 = text('''
		SELECT
			(
				(SELECT leftTime FROM GameEvents g2 JOIN Student s2 ON g2.studentId = s2.Id
					WHERE s2.classroomId = :classroomid AND status = 0 AND g1.gameplayId = g2.gameplayId)
				- (SELECT leftTime FROM GameEvents g2 JOIN Student s2 ON g2.studentId = s2.Id
					WHERE s2.classroomId = :classroomid AND status IN (2, 3, 4) AND g1.gameplayId = g2.gameplayId)
			) as duration,
			g1.date,
			g1.status,
			g1.score
			FROM GameEvents g1
			JOIN Student s1 ON g1.studentId = s1.Id
			WHERE s1.classroomId = :classroomid AND status IN (2, 3, 4)
	''')
	result = db.engine.execute(sql2, {'classroomid': classroomid + 0})

	statisticsResult = []
	for row in result:
		statisticsResult.append({
			'duration': row[0],
			'date': row[1],
			'status': row[2],
			'score': row[3]
		})

	return jsonify(statisticsResult)