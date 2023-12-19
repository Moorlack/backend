from flask import jsonify, request
from src.schema.user import CreateUserSchema, UserSchema
import src.services.user as service
import src.repositories.user as repositories


def create_user():
    data = request.get_json()
    dto = CreateUserSchema().load(data)

    response = service.create_user(dto)

    return jsonify(response), 201


def get_user_by_id(user_id):
    response = repositories.get_by_id(user_id)

    return jsonify(UserSchema().dump(obj=response))


def get_all_users():
    response = repositories.get_all_users()

    return jsonify(UserSchema().dump(obj=response, many=True))


def delete_user(user_id):
    service.delete_user_by_id(user_id)

    return jsonify({"success": True})

