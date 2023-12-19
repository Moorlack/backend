from flask import Blueprint, jsonify

app_routers = Blueprint('app', __name__)


@app_routers.app_errorhandler(404)
def page_not_found(err):
    return jsonify({'error': 'Not found'})
