from flask import request, abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
from application.auth.models import UserModel, RevokedTokenModel
from application import app
from utils.http import returns_json


@app.route('/v1/register', methods=['POST'])
@returns_json
def register():
    if not request.json:
        return {'message': 'No data'}, 400

    username = request.json['username']
    if UserModel.find_by_username(username):
        return {'message': f'User {username} already exists'}, 400

    new_user = UserModel(
        username=username,
        password=UserModel.generate_hash(request.json['password']))
    new_user.save_to_db()
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return {
        'message': f'User {username} was created',
        'access_token': access_token,
        'refresh_token': refresh_token
    }, 201


@app.route('/v1/login', methods=['POST'])
@returns_json
def login():
    if not request.json:
        return {'message': 'No data'}, 400
    username = request.json['username']
    current_user = UserModel.find_by_username(username)

    if not current_user:
        return {'message': f'User {username} doesn\'t exist'}, 400

    if UserModel.verify_hash(request.json['password'], current_user.password):
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return {
            'message': f'Logged in as {username}',
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
    else:
        return {'message': 'Wrong credentials'}, 421


@app.route('/v1/logout/access', methods=['POST'])
@returns_json
@jwt_required
def logout_access():
    jti = get_raw_jwt()['jti']
    revoked_token = RevokedTokenModel(jti=jti)
    revoked_token.add()
    return {'message': 'Access token has been revoked'}, 200


@app.route('/v1/logout/refresh', methods=['POST'])
@returns_json
@jwt_refresh_token_required
def logout_refresh():
    jti = get_raw_jwt()['jti']
    revoked_token = RevokedTokenModel(jti=jti)
    revoked_token.add()
    return {'message': 'Refresh token has been revoked'}, 200


@app.route('/v1/token/refresh', methods=['POST'])
@returns_json
@jwt_refresh_token_required
def token_refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}, 200
