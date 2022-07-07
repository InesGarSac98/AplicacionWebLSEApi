from flask import jsonify, Blueprint, request, make_response
import random
import string

# imports for PyJWT authentication
from selenium.webdriver.common.by import By
from sqlalchemy import text
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from .Models.classroom import Classroom

classrooms_controller = Blueprint("classrooms_controller", __name__, static_folder="Controllers")

from app import db

from .Services.token_services import allow_only_teachers, token_required


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
            'classroomCode': classroom.classroomCode
        })

    return jsonify(output)


@classrooms_controller.route('/<int:id>/', methods=['GET'])
@classrooms_controller.route('/<int:id>', methods=['GET'])
@token_required
def get_classroom(id):
    classroom = Classroom.query.filter(Classroom.id == id).first()

    return jsonify({
        'id': classroom.id,
        'teacherId': classroom.teacherId,
        'name': classroom.name,
        'classroomCode': classroom.classroomCode
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

    output = []
    for student in classroom.Students:
        output.append({
            'id': student.id,
            'user': {
                'name': student.User.name
            }
        })

    return jsonify(output)


@classrooms_controller.route('/<int:classroom_id>/words', methods=['GET'])
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


@classrooms_controller.route('/<int:classroom_id>/games', methods=['GET'])
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


@classrooms_controller.route('find-in-arasaac/<word>/', methods=['GET'])
@classrooms_controller.route('find-in-arasaac/<word>', methods=['GET'])
def findWordInArasaac_quizzGameQuestion(word):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    url = 'https://arasaac.org/lse/search/' + word
    driver.get(url)

    print(url)
    response = driver.find_element(By.TAG_NAME, 'html').text
    print(response)
    return make_response({'content': response}, 200)


@classrooms_controller.route('/<int:classroom_id>', methods=['DELETE'])
@classrooms_controller.route('<int:classroom_id>', methods=['DELETE'])
def delete_quizzGameQuestion(classroom_id):
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
		DELETE FROM Student WHERE classroomId = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    sql = text('''
		DELETE FROM Classroom WHERE Id = :classroomId;
	''')
    db.engine.execute(sql, {'classroomId': classroom_id})

    db.session.commit()
    return make_response()
