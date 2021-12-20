from app import config
from flask import request, jsonify, make_response
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return make_response({'message': 'Token no válido'}, 401)

        try:
            data = jwt.decode(token[7:], config['SECRET_KEY'], ["HS256"])
            current_user_id = data['user_id']

        except: return make_response({'message': 'Token no válido'}, 401)

        return f(current_user_id, *args, **kwargs)

    return decorator


