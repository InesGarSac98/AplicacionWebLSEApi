from flask import jsonify, Blueprint, request, make_response

# imports for PyJWT authentication
from .Models.quizzGameQuestion import QuizzGameQuestion
from .Models.quizzGameAnswer import QuizzGameAnswer
from .Services.token_services import token_required

quizzGameAnswers_controller = Blueprint("quizzGameAnswers_controller", __name__, static_folder="Controllers")

from app import db


@quizzGameAnswers_controller.route('/', methods=['POST'])
@quizzGameAnswers_controller.route('', methods=['POST'])
def create_quizzGameAnswer():
	new_quizzGameAnswer = request.get_json()
	data = dict(new_quizzGameAnswer)

	quizzGameAnswer = QuizzGameAnswer(**dict({
		'isCorrect': data['isCorrect'],
		'questionId': data['questionId'],
		'wordId': data['wordId'],
		'isImage': data['isImage']
	}))

	db.session.add(quizzGameAnswer)
	db.session.commit()
	return make_response(quizzGameAnswer.serialize())


@quizzGameAnswers_controller.route('/<int:answer_id>', methods=['PUT'])
@quizzGameAnswers_controller.route('<int:answer_id>', methods=['PUT'])
def update_quizzGameAnswer(answer_id):
	new_quizzGameAnswer = request.get_json()
	data = dict(new_quizzGameAnswer)

	quizzGameAnswer = QuizzGameAnswer(**data)

	if quizzGameAnswer.id != answer_id:
		make_response({}, 400)

	quizzGameAnswerFromDb = QuizzGameAnswer.query.filter(QuizzGameAnswer.id == answer_id).first()

	quizzGameAnswerFromDb.questionId = quizzGameAnswer.questionId
	quizzGameAnswerFromDb.wordId = quizzGameAnswer.wordId
	quizzGameAnswerFromDb.isImage = quizzGameAnswer.isImage
	quizzGameAnswerFromDb.isCorrect = quizzGameAnswer.isCorrect

	db.session.commit()
	return make_response(quizzGameAnswerFromDb.serialize())
