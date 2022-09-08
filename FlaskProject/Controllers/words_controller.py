from flask import jsonify, Blueprint, request, make_response

from .Models.student import Student
from .Models.teacher import Teacher
from .Models.words import Words
from .Services import search_in_arasaac_service
from .Services.token_services import token_required, token_required_get_user_id
from sqlalchemy import text, or_, null

words_controller = Blueprint("words_controller", __name__, static_folder="Controllers")
from app import db


@words_controller.route('/', methods=['GET'])
@words_controller.route('', methods=['GET'])
@token_required_get_user_id
def get_all_words(current_user_id):
    student = Student.query.filter(Student.userId == current_user_id).first()
    teacher = Teacher.query.filter(Teacher.userId == current_user_id).first()
    teacherId = None
    if student is not None:
        teacherId = student.Classroom.teacherId
    else:
        if teacher is not None:
            teacherId = teacher.id

    words = Words.query.filter(or_(Words.teacherId == teacherId, Words.teacherId == null())).all()
    output = []
    for word in words:
        output.append({
            'id': word.id,
            'teacherId': word.teacherId,
            'name': word.name,
            'image': word.image,
            'video': word.video,
            'videoDefinition': word.videoDefinition
        })

    return jsonify(output)


@words_controller.route('<word>/find-in-arasaac/', methods=['GET'])
@words_controller.route('<word>/find-in-arasaac/', methods=['GET'])
def find_word_in_arasaac(word):
    arasaacWord = search_in_arasaac_service.search(word)

    if arasaacWord is None:
        return make_response({'content': 'Palabra no encontrada en ARASAAC'}, 400)

    return make_response(arasaacWord, 200)


@words_controller.route('/', methods=['POST'])
@words_controller.route('', methods=['POST'])
@token_required
def create_word():
    new_word = request.get_json()
    data = dict(new_word)
    word = Words(**data)
    db.session.add(word)
    db.session.commit()
    return make_response(word.serialize())


@words_controller.route('/<int:word_id>', methods=['DELETE'])
@words_controller.route('<int:word_id>', methods=['DELETE'])
def delete_word(word_id):
    sql = text('''
        DELETE FROM QuizzGameAnswers WHERE questionId IN 
            (
                SELECT id FROM QuizzGameQuestions
                    WHERE wordId = :wordId
            );
    ''')
    db.engine.execute(sql, {'wordId': word_id})

    sql = text('''
        DELETE FROM QuizzGameQuestions WHERE wordId = :wordId;
    ''')
    db.engine.execute(sql, {'wordId': word_id})

    sql = text('''
        DELETE FROM QuizzGameAnswers WHERE questionId IN (SELECT questionId FROM QuizzGameAnswers WHERE wordId = :wordId);
    ''')
    db.engine.execute(sql, {'wordId': word_id})

    sql = text('''
        WITH questionIds AS (SELECT id FROM QuizzGameQuestions AS q WHERE NOT EXISTS(SELECT 1 FROM QuizzGameAnswers AS a WHERE a.questionId = q.id))
        DELETE FROM QuizzGameQuestions WHERE id IN questionIds;
    ''')
    db.engine.execute(sql)

    sql = text('''
        DELETE FROM StudentLearnedWords WHERE wordId = :wordId;
    ''')
    db.engine.execute(sql, {'wordId': word_id})

    sql = text('''
        DELETE FROM ClassroomWords WHERE wordId = :wordId;
    ''')
    db.engine.execute(sql, {'wordId': word_id})

    sql = text('''
        DELETE FROM Words WHERE id = :word_id;
    ''')
    db.engine.execute(sql, {'word_id': word_id})

    db.session.commit()
    return make_response()
