from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import src.controllers.category as controller
from src.errors.category import CategoryNotFound, UserAlreadyApproved
from src.errors.record import UserNotApprovedForCategory

category_routers = Blueprint('categories', __name__)


@category_routers.route('/api/category', methods=['POST'])
@jwt_required()
def create_category():
    return controller.create_category()


@category_routers.route('/api/category/<category_id>', methods=['GET'])
@jwt_required()
def get_category(category_id):
    return controller.get_category_by_id(category_id)


@category_routers.route('/api/category/<category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    return controller.delete_category_by_id(category_id)


@category_routers.route('/api/category/user', methods=['PATCH'])
@jwt_required()
def approve_user():
    return controller.add_approved_user()


@category_routers.app_errorhandler(CategoryNotFound)
def user_not_found(err):
    return jsonify({'error': 'Category not found'}), 404


@category_routers.app_errorhandler(UserNotApprovedForCategory)
def user_not_approved_for_category(err):
    return jsonify({'error': 'User not approved for category'}), 400


@category_routers.app_errorhandler(UserAlreadyApproved)
def user_already_approved(err):
    return jsonify({'error': 'User already approved to use this category'}), 400
