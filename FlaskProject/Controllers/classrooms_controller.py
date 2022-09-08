from flask import jsonify, Blueprint, request, make_response
from sqlalchemy import text
import random
import string


from .Models.classroom import Classroom
from .Services.token_services import allow_only_teachers, token_required

classrooms_controller = Blueprint("classrooms_controller", __name__, static_folder="Controllers")
from app import db


@classrooms_controller.route('/<int:id>/', methods=['GET'])
@classrooms_controller.route('/<int:id>', methods=['GET'])
@token_required
def get_classroom(id):
    classroom = Classroom.query.filter(Classroom.id == id).first()
    if classroom is None:
        return make_response("Clase no encontrada", 404)

    return jsonify(classroom.serialize())


@classrooms_controller.route('/', methods=['POST'])
@classrooms_controller.route('', methods=['POST'])
@allow_only_teachers
def create_classroom():
    new_classroom = request.get_json()
    data = dict(new_classroom)
    classroom = Classroom(**data)

    if classroom.teacherId is None:
        return make_response("El campo teacherId es obligatorio", 400)
    if classroom.name is None:
        return make_response("El campo name es obligatorio", 400)

    classroom.classroomCode = generate_new_unique_classroom_code()
    db.session.add(classroom)
    db.session.commit()
    return make_response(classroom.serialize())


def generate_new_unique_classroom_code():
    characters = string.ascii_letters + \
                 string.digits + \
                 string.punctuation + \
                 string.ascii_lowercase + \
                 string.ascii_uppercase
    code = ''.join(random.choice(characters) for i in range(10))

    return code


@classrooms_controller.route('/<int:classroom_id>/students', methods=['GET'])
@allow_only_teachers
def get_all_classroom_students(classroom_id):
    classroom = Classroom.query.filter(Classroom.id == classroom_id).first()

    if classroom is None:
        return make_response("Clase no encontrada", 404)

    output = []
    for student in classroom.Students:
        output.append(student.serialize())

    return jsonify(output)


@classrooms_controller.route('/<int:classroom_id>/words', methods=['GET'])
@token_required
def get_all_classroom_words(classroom_id):
    classroom = Classroom.query.filter(Classroom.id == classroom_id).first()

    if classroom is None:
        return make_response("Clase no encontrada", 404)

    output = []
    for classroomWord in classroom.ClassroomWords:
        output.append(classroomWord.serialize())

    return jsonify(output)


@classrooms_controller.route('/<int:classroom_id>/games', methods=['GET'])
@token_required
def get_all_classroom_games(classroom_id):
    classroom = Classroom.query.filter(Classroom.id == classroom_id).first()

    if classroom is None:
        return make_response("Clase no encontrada", 404)

    output = []
    for classroomGame in classroom.ClassroomGames:
        output.append(classroomGame.serialize())

    return jsonify(output)


@classrooms_controller.route('/<int:classroom_id>', methods=['DELETE'])
@classrooms_controller.route('<int:classroom_id>', methods=['DELETE'])
@allow_only_teachers
def delete_classroom(classroom_id):
    sql = text('''
		DELETE FROM QuizzGameAnswers WHERE questionId IN 
			(
				SELECT id FROM QuizzGameQuestions
					WHERE quizzGameClassroomConfigurationId IN 
					(
						SELECT Id FROM QuizzGameClassroomConfiguration
							WHERE classroomId = :classroomId
					)
			);
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM QuizzGameQuestions WHERE quizzGameClassroomConfigurationId IN 
			(
				SELECT Id FROM QuizzGameClassroomConfiguration
					WHERE classroomId = :classroomId
			);
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM QuizzGameClassroomConfiguration WHERE classroomId = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM MemoryGameClassroomConfiguration WHERE classroomId = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM ClassroomGames WHERE classroomId = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM ClassroomWords WHERE classroomId = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM GameEvents WHERE studentId IN 
			(
				SELECT id FROM Student
					WHERE classroomId = :classroomId
			);
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM User WHERE Id IN 
			(
				SELECT userId FROM Student
					WHERE classroomId = :classroomId
			);
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
        DELETE FROM StudentLearnedWords WHERE studentId IN (SELECT id FROM Student WHERE classroomId = :classroomId);
    ''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM Student WHERE classroomId = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM Classroom WHERE Id = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    db.session.commit()
    return make_response()
