import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['DEBUG'] = True
app.debug = True
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_message = 'You do not have permission to access that page. Please Log in to continue.'
login_manager.login_message_category = 'danger'
login_manager.login_view = 'home'

from flask import Flask
from flask_s3 import FlaskS3
app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'movie-catalogapp-bucket2'
s3 = FlaskS3(app)
s3.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()