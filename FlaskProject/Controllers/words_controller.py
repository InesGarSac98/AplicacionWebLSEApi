from flask import jsonify, Blueprint, request, make_response
from .Models.words import Words

words_controller = Blueprint("words_controller", __name__, static_folder="Controllers")
from app import db


@words_controller.route('/', methods=['GET'])
@words_controller.route('', methods=['GET'])
def get_all_words():
    words = Words.query.all()
    output = []
    for word in words:
        output.append({
            'id': word.id,
            'url': word.url,
            'name': word.url
        })

    return jsonify(output)


@words_controller.route('/', methods=['POST'])
@words_controller.route('', methods=['POST'])
# @token_required
def create_word():
    new_word = request.get_json()
    data = dict(new_word)
    word = Words(**data)
    db.session.add(word)
    db.session.commit()
    return make_response(word.serialize())
