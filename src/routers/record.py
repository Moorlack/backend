from flask import Blueprint
from ..controllers.record import *
from ..errors.record import RecordNotFound

record_routers = Blueprint('records', __name__)

record_routers.route('/api/record', methods=['POST'])(create_record)
record_routers.route('/api/record/<record_id>', methods=['GET'])(get_record_by_id)
record_routers.route('/api/records', methods=['GET'])(get_records_by_filters)
record_routers.route('/api/record/<record_id>', methods=['DELETE'])(delete_record_by_id)


@record_routers.app_errorhandler(RecordNotFound)
def user_not_found(err):
    return jsonify({'message': 'Record not found'}), 404
