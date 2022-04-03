from flask import jsonify, Blueprint, request, make_response

# imports for PyJWT authentication
from .Models.quizzGameQuestion import QuizzGameQuestion
from .Services.token_services import token_required

quizzGameQuestions_controller = Blueprint("quizzGameQuestions_controller", __name__, static_folder="Controllers")

from app import db


@quizzGameQuestions_controller.route('/', methods=['GET'])
@token_required
def get_questions():
	wordIdsCommaSeparatedString = request.args.get("wordIds")
	if not wordIdsCommaSeparatedString or wordIdsCommaSeparatedString == '':
		questions = QuizzGameQuestion.query.all()
	else:
		wordIds = wordIdsCommaSeparatedString.split(',')
		questions = QuizzGameQuestion.query.filter(QuizzGameQuestion.wordId.in_(wordIds)).all()

	output = []
	for question in questions:
		output.append(question.serialize())

	return jsonify(output)


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


@quizzGameQuestions_controller.route('/<question_id>', methods=['PUT'])
@quizzGameQuestions_controller.route('<question_id>', methods=['PUT'])
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


@quizzGameQuestions_controller.route('/<question_id>', methods=['DELETE'])
@quizzGameQuestions_controller.route('<question_id>', methods=['DELETE'])
def delete_quizzGameQuestion(question_id):
	QuizzGameQuestion.query.filter(QuizzGameQuestion.id == question_id).delete()
	db.session.commit()
	return make_response()
