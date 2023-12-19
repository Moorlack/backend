from flask import Blueprint
from ..controllers.auth import *
from ..errors.auth import InvalidCredentialsError

auth_routers = Blueprint('auth', __name__)

auth_routers.route('/api/login', methods=['POST'])(login)


@auth_routers.app_errorhandler(InvalidCredentialsError)
def invalid_credentials(err):
    return jsonify({'error': 'Invalid credentials'}), 400
