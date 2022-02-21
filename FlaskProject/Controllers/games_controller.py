from flask import jsonify, Blueprint, request, make_response
import json

# imports for PyJWT authentication
from .Models.games import Games

games_controller = Blueprint("games_controller", __name__, static_folder="Controllers")

from app import db


@games_controller.route('/', methods=['POST'])
@games_controller.route('', methods=['POST'])
# @token_required
def create_game():
	new_game = request.get_json()
	data = dict(new_game)
	game = Games(**data)
	db.session.add(game)
	db.session.commit()
	return make_response(game.serialize())


