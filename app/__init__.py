import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from settings import Config


# init application of the Flask
app = Flask(__name__)
app.config.from_object(Config)

# configure the SQLite database, relative to the app instance folder
db = SQLAlchemy()
db.init_app(app)

from app.models import User

login_manager = LoginManager(app)
login_manager.login_view = "login"


# login_manager.login_message = "NEED LOGIN"
# login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id: int):
    return db.session.execute(db.select(User).where(User.id == int(user_id))).scalar()

from app.routes import *
