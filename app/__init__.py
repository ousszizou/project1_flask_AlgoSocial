# import flask & important modules/extensions
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask, render_template
from dotenv import load_dotenv
import config
import os
from flask_login import LoginManager
from flask_restful import Api
from flask_marshmallow import Marshmallow

# create app object
app = Flask(__name__)

# define ma
ma = Marshmallow(app)

# create API
api = Api(app)
from app.API.resources import UserResource
api.add_resource(UserResource, '/api/users')

# Environment configurations
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))

# Database
from app.models import db, users
from app.models.users import User
from app.models.posts import Post

db.create_all()
db.session.commit()

# migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Small HTTP Error Handling
@app.errorhandler(404)
def not_found(error):
    title = 'page not found'
    return render_template('errors/404.html', title=title), 404

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Blueprints
# blueprint for non-auth parts of app
from app.views.home import home as home_blueprint

# blueprint for auth parts of app
from app.views.auth import auth as auth_blueprint

# Register Blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
