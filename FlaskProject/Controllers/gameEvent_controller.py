from datetime import datetime

from flask import Blueprint, request, make_response

# imports for PyJWT authentication
from .Models.gameEvent import GameEvent
from .Services.token_services import allow_only_students, token_required

gameEvent_controller = Blueprint("gameEvent_controller", __name__, static_folder="Controllers")


from app import db


@gameEvent_controller.route('/', methods=['POST'])
@gameEvent_controller.route('', methods=['POST'])
@allow_only_students
def create_gameEvent():
	new_gameEvent = request.get_json()
	data = dict(new_gameEvent)
	gameEvent = GameEvent(**data)
	gameEvent.date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f%z')

	if gameEvent.status == 0:
		gameEventWithMaxGamePlayId = GameEvent.query.order_by(GameEvent.gamePlayId.desc()).first()
		if not gameEventWithMaxGamePlayId:
			gameplayId = 1
		else:
			gameplayId = gameEventWithMaxGamePlayId.gamePlayId + 1
		gameEvent.gamePlayId = gameplayId

	db.session.add(gameEvent)
	db.session.commit()
	return make_response(gameEvent.serialize())
