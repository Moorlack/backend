from flask import request, jsonify
from werkzeug.exceptions import BadRequest

from src.schema.record import CreateRecordSchema, RecordSchema
import src.services.record as service
import src.repositories.record as repository


def create_record():
    data = request.get_json()
    dto = CreateRecordSchema().load(data)

    response = service.create_record(dto)

    return jsonify(response), 201


def get_record_by_id(record_id):
    response = repository.get_record_by_id(record_id)

    return jsonify(RecordSchema().dump(obj=response))


def get_records_by_filters():
    data = request.get_json()

    if 'user_id' not in data and 'category_id' not in data:
        raise BadRequest('You should provide at least user id or category id')

    response = repository.get_records_by_filter(data)

    return jsonify(RecordSchema().dump(obj=response, many=True))


def delete_record_by_id(record_id):
    service.delete_record_by_id(record_id)
    return jsonify({'success': True})
