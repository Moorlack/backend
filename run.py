from os import getenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from src.routers.auth import auth_routers
from src.routers.category import category_routers
from src.routers.record import record_routers
from src.utils.db import db
from src.routers.healthcheck import healthcheck_routers
from src.routers.app import app_routers
from src.routers.user import user_routers
from src.utils.jwt_handlers import setup_jwt_handlers
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')

app.register_blueprint(healthcheck_routers)
app.register_blueprint(app_routers)
app.register_blueprint(user_routers)
app.register_blueprint(category_routers)
app.register_blueprint(record_routers)
app.register_blueprint(auth_routers)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from src.models import user
from src.models import category
from src.models import record

setup_jwt_handlers(jwt)

if __name__ == "__main__":
    app.run(debug=getenv('DEBUG') == 'true', port=getenv('PORT') or '5050', host=getenv('HOST') or '0.0.0.0')
