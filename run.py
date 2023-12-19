from os import getenv
from flask import Flask
from flask_migrate import Migrate
from src.routers.category import category_routers
from src.utils.db import db
from src.routers.healthcheck import healthcheck_routers
from src.routers.app import app_routers
from src.routers.user import user_routers
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')

app.register_blueprint(healthcheck_routers)
app.register_blueprint(app_routers)
app.register_blueprint(user_routers)
app.register_blueprint(category_routers)

db.init_app(app)
migrate = Migrate(app, db)

from src.models import user
from src.models import category

if __name__ == "__main__":
    app.run(debug=True)
