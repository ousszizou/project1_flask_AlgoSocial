# import flask & important modules/extensions
from flask import Flask, render_template
from dotenv import load_dotenv
import config
import os

# create app object
app = Flask(__name__)

# Environment configurations
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get('ENV'))



# Database
from app.models import db, users

db.create_all()
db.session.commit()

# Small HTTP Error Handling
@app.errorhandler(404)
def not_found(error):
    title = 'page not found'
    return render_template('errors/404.html', title=title), 404

# Blueprints
# blueprint for non-auth parts of app
from app.views.home import home as home_blueprint

# blueprint for auth parts of app
from app.views.auth import auth as auth_blueprint

# Register Blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
