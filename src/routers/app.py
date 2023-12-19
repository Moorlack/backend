from marshmallow.exceptions import ValidationError
from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

app_routers = Blueprint('app', __name__)


@app_routers.app_errorhandler(HTTPException)
def bad_request(err: HTTPException):
    return jsonify({'message': err.description}), err.code


@app_routers.app_errorhandler(ValidationError)
def validation_error(err: ValidationError):
    return jsonify({'error': 'Failure validation', 'rules': err.messages}), 415
