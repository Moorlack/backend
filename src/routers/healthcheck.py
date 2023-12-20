from flask import jsonify, Blueprint

healthcheck_routers = Blueprint('healthcheck', __name__)


@healthcheck_routers.get('/api/healthcheck')
def healthcheck():
    return jsonify({'status': 'ok'})


@healthcheck_routers.route("/api")
def homepage():
    response = "<h1 style='white-space: nowrap'>Back-end goes b" + "r" * 5000 + "</h1>"
    return response, 200
