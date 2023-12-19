from flask import request, jsonify
from src.schema.category import CategorySchema, CategoryCreateSchema
import src.services.category as service
import src.repositories.category as repository


def create_category():
    data = request.get_json()
    dto = CategoryCreateSchema().load(data)

    response = service.create_category(dto)

    return jsonify(response)


def get_category_by_id(category_id):
    category = repository.get_category_by_id(category_id)

    return jsonify(CategorySchema().dump(category))


def delete_category_by_id(category_id):
    service.delete_category(category_id)

    return jsonify({'success': True})