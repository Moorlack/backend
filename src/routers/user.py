from flask import Blueprint
from ..controllers.user import *
from src.errors.user import UserAlreadyExistsError, UserNotFoundError

user_routers = Blueprint('users', __name__)

user_routers.route('/api/user', methods=['POST'])(create_user)
user_routers.route('/api/users', methods=['GET'])(get_all_users)
user_routers.route('/api/user/<user_id>', methods=['GET'])(get_user_by_id)
user_routers.route('/api/user/<user_id>', methods=['DELETE'])(delete_user)


@user_routers.errorhandler(UserAlreadyExistsError)
def user_already_exists(err):
    return jsonify({'message': 'User with this name already exists'}), 400


@user_routers.errorhandler(UserNotFoundError)
def user_not_found(err):
    return jsonify({'message': 'User not found'}), 404
