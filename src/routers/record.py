from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import src.controllers.record as controller
from ..errors.record import RecordNotFound

record_routers = Blueprint('records', __name__)


@record_routers.route('/api/record', methods=['POST'])
@jwt_required()
def create_record():
    controller.create_record()


@record_routers.route('/api/record/<record_id>', methods=['GET'])
@jwt_required()
def get_record(record_id):
    controller.get_record_by_id(record_id)


@record_routers.route('/api/records', methods=['GET'])
def get_records_by_filter():
    controller.get_records_by_filters()


@record_routers.route('/api/record/<record_id>', methods=['DELETE'])
@jwt_required()
def delete_record(record_id):
    controller.delete_record_by_id(record_id)


@record_routers.app_errorhandler(RecordNotFound)
def user_not_found(err):
    return jsonify({'error': 'Record not found'}), 404
