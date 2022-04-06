from flask import jsonify, Blueprint, request, make_response

# imports for PyJWT authentication
from .Models.quizzGameClassroomConfiguration import QuizzGameClassroomConfiguration
from .Models.quizzGameQuestion import QuizzGameQuestion
from .Models.quizzGameAnswer import QuizzGameAnswer
from .Services.token_services import token_required

quizzGameClassroomConfiguration_controller = Blueprint("quizzGameClassroomConfiguration", __name__, static_folder="Controllers")

from app import db


@quizzGameClassroomConfiguration_controller.route('/', methods=['GET'])
@token_required
def get_quizzConfiguration():
	classroomId = request.args.get("classroomId")
	quizzConfiguration = QuizzGameClassroomConfiguration.query.\
		filter(QuizzGameClassroomConfiguration.classroomId == classroomId).first()

	if not quizzConfiguration:
		return make_response({'message': 'No quizzConfiguration found'}, 404)

	return make_response(quizzConfiguration.serialize())


@quizzGameClassroomConfiguration_controller.route('/', methods=['POST'])
@quizzGameClassroomConfiguration_controller.route('', methods=['POST'])
def create_quizzConfiguration():
	new_quizzConfiguration = request.get_json()
	data = dict(new_quizzConfiguration)

	quizzConfiguration = QuizzGameClassroomConfiguration(**data)

	db.session.add(quizzConfiguration)
	db.session.commit()
	return make_response(quizzConfiguration.serialize())


@quizzGameClassroomConfiguration_controller.route('/<int:configuration_id>', methods=['PUT'])
@quizzGameClassroomConfiguration_controller.route('<int:configuration_id>', methods=['PUT'])
def update_quizzGameQuestion(configuration_id):
	new_quizzGameConfig = request.get_json()
	data = dict(new_quizzGameConfig)

	quizzGameConfig = QuizzGameClassroomConfiguration(**data)

	if quizzGameConfig.id != configuration_id:
		make_response({}, 400)

	quizzGameClassroomConfiguration = QuizzGameClassroomConfiguration.query\
		.filter(QuizzGameClassroomConfiguration.id == configuration_id)\
		.first()

	quizzGameClassroomConfiguration.time = quizzGameConfig.time

	db.session.commit()
	return make_response(quizzGameClassroomConfiguration.serialize())
