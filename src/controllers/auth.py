from flask import request, jsonify
from src.schema.auth import LoginSchema
import src.services.auth as service


def login():
    data = request.get_json()
    dto = LoginSchema().load(data)

    response = service.login(dto)

    return jsonify(response)
