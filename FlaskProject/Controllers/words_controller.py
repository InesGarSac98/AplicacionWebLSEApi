from flask import jsonify, Blueprint, request, make_response
from sqlalchemy.sql.elements import and_, or_

from .Models.classroom import Classroom
from .Models.words import Words
from .Services import search_in_arasaac_service
from .Services.token_services import token_required, allow_only_teachers
from sqlalchemy import text
words_controller = Blueprint("words_controller", __name__, static_folder="Controllers")
from app import db


@words_controller.route('/', methods=['GET'])
@words_controller.route('', methods=['GET'])
@token_required
def get_all_words():
    teacherId = request.args.get("teacherId")
    words = Words.query.all()
    # words = Words.query.filter(or_(Words.teacherId == teacherId, Words.teacherId is None)).all()
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


@words_controller.route('/<wordname>/', methods=['GET'])
@words_controller.route('/<wordname>', methods=['GET'])
@token_required
def get_word(wordname):
    word = Words.query.filter(Words.name == wordname).first()
    output = {
        'id': word.id,
        'teacherId': word.teacherId,
        'name': word.name,
        'image': word.image,
        'video': word.video,
        'videoDefinition': word.videoDefinition
    }

    return jsonify(output)


@words_controller.route('<word>/find-in-arasaac/', methods=['GET'])
@words_controller.route('<word>/find-in-arasaac/', methods=['GET'])
def findWordInArasaac_quizzGameQuestion(word):
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
        DELETE FROM Words WHERE id = :word_id;
    ''')
    db.engine.execute(sql, {'word_id': word_id})

    db.session.commit()
    return make_response()
