from flask import jsonify, Blueprint, request

# imports for PyJWT authentication
from .Models.memoryGameClassroomConfiguration import MemoryGameClassroomConfiguration
from .Models.quizzGameClassroomConfiguration import QuizzGameClassroomConfiguration
from .Models.quizzGameQuestion import QuizzGameQuestion
from .Models.quizzGameAnswer import QuizzGameAnswer
from .Services.token_services import token_required

memoryGameClassroomConfiguration_controller = Blueprint("memoryGameClassroomConfiguration", __name__, static_folder="Controllers")

from app import db


@memoryGameClassroomConfiguration_controller.route('/', methods=['GET'])
@token_required
def get_memoryConfiguration():
	memoryConfiguration = MemoryGameClassroomConfiguration.query.filter(QuizzGameClassroomConfiguration.id == id).first()

	return jsonify({
		'id': memoryConfiguration.id,
		'classroomId': memoryConfiguration.teacherId,
		'gameId': memoryConfiguration.name,
		'time': memoryConfiguration.name
	})
