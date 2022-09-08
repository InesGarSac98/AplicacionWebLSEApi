from flask import jsonify, Blueprint, request, make_response
from datetime import datetime

from sqlalchemy import and_

from .Models.studentLearnedWords import StudentLearnedWords
from .Services.token_services import token_required, allow_only_students

student_learned_words_controller = Blueprint("student_learned_words_controller", __name__, static_folder="Controllers")

from app import db


@student_learned_words_controller.route('/', methods=['GET'])
@student_learned_words_controller.route('', methods=['GET'])
@token_required
def get_all():
    studentId = request.args.get("studentId")

    if studentId is None or studentId == '':
        return make_response({'message':'StudentId is required'}, 400)

    learned_words = StudentLearnedWords.query.filter(StudentLearnedWords.studentId == studentId)
    output = []
    for learned_word in learned_words:
        output.append(learned_word.serialize())

    return jsonify(output)


@student_learned_words_controller.route('/', methods=['POST'])
@student_learned_words_controller.route('', methods=['POST'])
@allow_only_students
def save_student_learned_word():
    new_learned_word = request.get_json()
    data = dict(new_learned_word)
    learned_word = StudentLearnedWords(**data)

    existingLearnedWord = StudentLearnedWords.query.filter(and_(StudentLearnedWords.studentId == learned_word.studentId, StudentLearnedWords.wordId == learned_word.wordId)).first()

    if existingLearnedWord is not None:
        return make_response(existingLearnedWord.serialize())

    learned_word.date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f%z')

    db.session.execute('PRAGMA foreign_keys = ON;')
    db.session.add(learned_word)
    db.session.commit()
    return make_response(learned_word.serialize())
