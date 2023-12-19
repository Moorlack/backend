from flask import Blueprint
from ..controllers.category import *
from ..errors.category import CategoryNotFound, UserAlreadyApproved

category_routers = Blueprint('categories', __name__)

category_routers.route('/api/category', methods=['POST'])(create_category)
category_routers.route('/api/category/<category_id>', methods=['GET'])(get_category_by_id)
category_routers.route('/api/category/<category_id>', methods=['DELETE'])(delete_category_by_id)
category_routers.route('/api/category/user', methods=['PATCH'])(add_approved_user)


@category_routers.app_errorhandler(CategoryNotFound)
def user_not_found(err):
    return jsonify({'error': 'Category not found'}), 404


@category_routers.app_errorhandler(UserAlreadyApproved)
def user_already_approved(err):
    return jsonify({'error': 'User already approved to use this category'}), 400
