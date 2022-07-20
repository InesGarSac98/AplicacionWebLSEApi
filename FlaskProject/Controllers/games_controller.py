from flask import jsonify, Blueprint, request, make_response
import json

# imports for PyJWT authentication
from .Models.games import Games
from .Services.token_services import token_required, allow_only_teachers

games_controller = Blueprint("games_controller", __name__, static_folder="Controllers")

from app import db


@games_controller.route('/', methods=['GET'])
@games_controller.route('', methods=['GET'])
@allow_only_teachers
def get_all_games():
    games = Games.query.all()
    output = []
    for game in games:
        output.append({
            'id': game.id,
            'name': game.name,
            'image': game.image
        })

    return jsonify(output)

