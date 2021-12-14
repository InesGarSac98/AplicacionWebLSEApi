from flask import jsonify, Blueprint, request, make_response
import json

from .Models.studentAvailableGame import studentAvailableGame

studentAvailableGame_controller = Blueprint("studentAvailableGame_controller", __name__, static_folder="Controllers")

from app import db


@studentAvailableGame_controller.route('/', methods=['GET'])
# @token_required
# def get_all_users(current_user):
def get_all_studentsAvailableGames():
    # querying the database
    # for all the entries in it
    studentAvailable = studentAvailableGame.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for studentAvGa in studentAvailable:
        # appending the user data json
        # to the response list
        output.append({
            'userId': studentAvGa.userId,
            'classroomCode': studentAvGa.classroomCode
        })

    return jsonify(output)


@studentAvailableGame_controller.route('/', methods=['POST'])
@studentAvailableGame_controller.route('', methods=['POST'])
# @token_required
def create_studentAvailable():
    new_studentAvailable = request.get_json()
    data = dict(new_studentAvailable)
    studentAvailable = studentAvailableGame(**data)
    db.session.add(studentAvailable)
    db.session.commit()
    return make_response(studentAvailable.serialize())
