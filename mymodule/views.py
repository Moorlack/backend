from flask import jsonify
from mymodule import app

@app.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'ok'})
