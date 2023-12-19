from flask import Flask
from src.routers.healthcheck import healthcheck_routers
from src.routers.app import app_routers

app = Flask(__name__)

app.register_blueprint(healthcheck_routers)
app.register_blueprint(app_routers)

app.run(debug=True)
