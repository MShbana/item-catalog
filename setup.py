import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_message = 'You do not have permission to access this page. Please Log in to continue.'
login_manager.login_message_category = 'danger'
login_manager.login_view = 'google_login'
