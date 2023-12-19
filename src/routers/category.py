from flask import Blueprint
from ..controllers.category import *
from ..errors.category import CategoryNotFound

category_routers = Blueprint('categories', __name__)

category_routers.route('/api/category', methods=['POST'])(create_category)
category_routers.route('/api/category/<category_id>', methods=['GET'])(get_category_by_id)
category_routers.route('/api/category/<category_id>', methods=['DELETE'])(delete_category_by_id)


@category_routers.app_errorhandler(CategoryNotFound)
def user_not_found(err):
    return jsonify({'message': 'Category not found'}), 404
