from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import src.controllers.user as controller
from src.errors.user import UserAlreadyExistsError, UserNotFoundError

user_routers = Blueprint('users', __name__)


@user_routers.route('/api/user', methods=['POST'])
def create_user():
    return controller.create_user()


@user_routers.route('/api/users', methods=['GET'])
@jwt_required()
def get_users():
    return controller.get_all_users()


@user_routers.route('/api/user/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return controller.get_user_by_id(user_id)


@user_routers.route('/api/user/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return controller.delete_user(user_id)


@user_routers.app_errorhandler(UserAlreadyExistsError)
def user_already_exists(err):
    return jsonify({'error': 'User with this name already exists'}), 400


@user_routers.app_errorhandler(UserNotFoundError)
def user_not_found(err):
    return jsonify({'error': 'User not found'}), 404
