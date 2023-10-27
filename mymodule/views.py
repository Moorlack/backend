from flask import jsonify
from mymodule import app

@app.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'ok'})

@app.route("/")
def homepage():
    response = "<h1>Back-end goes brrr</h1>"
    return response, 200
