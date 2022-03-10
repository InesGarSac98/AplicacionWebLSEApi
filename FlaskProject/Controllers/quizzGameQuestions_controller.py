from flask import jsonify, Blueprint, request

# imports for PyJWT authentication
from .Models.quizzGameQuestion import QuizzGameQuestion
from .Models.quizzGameAnswer import QuizzGameAnswer
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
