import jwt
from flask import jsonify, Blueprint, request, make_response
import datetime

from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

users_controller = Blueprint("users_controller", __name__, static_folder="Controllers")

from .Models.user import User
from app import db, config

from .Services.token_services import token_required, token_required_get_user_id


@users_controller.route('/', methods=['POST'])
@users_controller.route('', methods=['POST'])
# @token_required
def create_user():
    new_user = request.get_json()
    data = dict(new_user)
    if not 'name' in data:
        return make_response('El campo nombre es obligatorio', 400)
    if not 'password' in data:
        return make_response('El campo password es obligatorio', 400)
    if not 'email' in data:
        return make_response('El campo email es obligatorio', 400)
    if not 'role' in data:
        return make_response('El campo role es obligatorio', 400)

    hashed_password = generate_password_hash(data['password'], method='sha256')

    user = User(name=data['name'], password=hashed_password, email=data['email'], role=data['role'])

    existingUser = User.query.filter(or_(User.name == user.name, User.email == user.email)).count()
    if existingUser > 0:
        return make_response('El usuario ya existe', 400)

    db.session.add(user)
    db.session.commit()
    return make_response(user.serialize())


# Permitir que los usuarios registrados puedan iniciar sesión
@users_controller.route('/login', methods=['POST'])
@users_controller.route('/login/', methods=['POST'])
def login_user():
    auth = dict(request.get_json())

    if not auth or 'name' not in auth or not auth['name'] or 'password' not in auth or not auth['password']:
        return make_response('Usuario y contraseña obligatorios', 400)

    user = User.query.filter_by(name=auth['name']).first()

    if not user:
        return make_response('Usuario y contraseña incorrectos.', 401)

    if check_password_hash(user.password, auth['password']):
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        token = jwt.encode(
            {
                'user_id': user.id,
                'role': user.role,
                'exp': exp.utcfromtimestamp(exp.timestamp())
            },
            config['SECRET_KEY']
        ) + ''
        return make_response({'token': token}, 200)

    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


@users_controller.route('/user-loged', methods=['GET'])
@users_controller.route('/user-loged/', methods=['GET'])
@token_required_get_user_id
# def get_all_users(current_user):
def get_user_logged(current_user_id):
    user = User.query.filter_by(id=current_user_id).first()

    return jsonify({
        'name': user.name,
        'email': user.email,
        'id': user.id,
        'role': user.role
    })


@users_controller.route('/validate-token', methods=['POST'])
@users_controller.route('/validate-token/', methods=['POST'])
@token_required
def validate_token():
    return make_response('', 200)
