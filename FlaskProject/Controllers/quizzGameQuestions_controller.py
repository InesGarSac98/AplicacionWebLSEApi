from flask import jsonify, Blueprint, request, make_response

from .Models.quizzGameAnswer import QuizzGameAnswer
from .Models.quizzGameQuestion import QuizzGameQuestion
from .Services.token_services import token_required

quizzGameQuestions_controller = Blueprint("quizzGameQuestions_controller", __name__, static_folder="Controllers")

from app import db


@quizzGameQuestions_controller.route('/', methods=['POST'])
@quizzGameQuestions_controller.route('', methods=['POST'])
def create_quizzGameQuestion():
	new_quizzGameQuestion = request.get_json()
	data = dict(new_quizzGameQuestion)

	quizzGameQuestion = QuizzGameQuestion(**dict({
		'name': data['name'],
		'wordId': data['wordId'],
		'quizzGameClassroomConfigurationId': data['quizzGameClassroomConfigurationId'],
		'isImage': data['isImage']
	}))

	db.session.add(quizzGameQuestion)
	db.session.commit()
	return make_response(quizzGameQuestion.serialize())


@quizzGameQuestions_controller.route('/<int:question_id>', methods=['PUT'])
@quizzGameQuestions_controller.route('<int:question_id>', methods=['PUT'])
def update_quizzGameQuestion(question_id):
	new_quizzGameQuestion = request.get_json()
	data = dict(new_quizzGameQuestion)

	quizzGameQuestion = QuizzGameQuestion(**data)

	if quizzGameQuestion.id != question_id:
		make_response({}, 400)

	quizzGameQuestionFromDb = QuizzGameQuestion.query.filter(QuizzGameQuestion.id == question_id).first()

	quizzGameQuestionFromDb.name = quizzGameQuestion.name
	quizzGameQuestionFromDb.wordId = quizzGameQuestion.wordId
	quizzGameQuestionFromDb.isImage = quizzGameQuestion.isImage

	db.session.commit()
	return make_response(quizzGameQuestionFromDb.serialize())


@quizzGameQuestions_controller.route('/<int:question_id>', methods=['DELETE'])
@quizzGameQuestions_controller.route('<int:question_id>', methods=['DELETE'])
def delete_quizzGameQuestion(question_id):
	QuizzGameAnswer.query.filter(QuizzGameAnswer.questionId == question_id).delete()

	QuizzGameQuestion.query.filter(QuizzGameQuestion.id == question_id).delete()
	db.session.commit()
	return make_response()
