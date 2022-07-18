from flask import Blueprint, request, make_response

from .Models.memoryGameClassroomConfiguration import MemoryGameClassroomConfiguration
from .Services.token_services import token_required

memoryGameClassroomConfiguration_controller = Blueprint("memoryGameClassroomConfiguration", __name__, static_folder="Controllers")

from app import db


@memoryGameClassroomConfiguration_controller.route('/', methods=['GET'])
@memoryGameClassroomConfiguration_controller.route('', methods=['GET'])
@token_required
def get_memoryConfiguration():
	classroomId = request.args.get("classroomId")
	memoryConfiguration = MemoryGameClassroomConfiguration.query.\
		filter(MemoryGameClassroomConfiguration.classroomId == classroomId).first()

	if not memoryConfiguration:
		return make_response({'message': '-----No memoryConfiguration found'}, 404)

	return make_response(memoryConfiguration.serialize())


@memoryGameClassroomConfiguration_controller.route('/', methods=['POST'])
@memoryGameClassroomConfiguration_controller.route('', methods=['POST'])
def create_memoryConfiguration():
	new_memoryConfiguration = request.get_json()
	data = dict(new_memoryConfiguration)

	memoryConfiguration = MemoryGameClassroomConfiguration(**data)

	db.session.add(memoryConfiguration)
	db.session.commit()
	return make_response(memoryConfiguration.serialize())


@memoryGameClassroomConfiguration_controller.route('/<int:configuration_id>', methods=['PUT'])
@memoryGameClassroomConfiguration_controller.route('<int:configuration_id>', methods=['PUT'])
def update_memoryGameQuestion(configuration_id):
	new_memoryGameConfig = request.get_json()
	data = dict(new_memoryGameConfig)

	memoryGameConfig = MemoryGameClassroomConfiguration(**data)

	if memoryGameConfig.id != configuration_id:
		make_response({}, 400)

	memoryGameClassroomConfiguration = MemoryGameClassroomConfiguration.query\
		.filter(MemoryGameClassroomConfiguration.id == configuration_id)\
		.first()

	memoryGameClassroomConfiguration.time = memoryGameConfig.time

	db.session.commit()
	return make_response(memoryGameClassroomConfiguration.serialize())
