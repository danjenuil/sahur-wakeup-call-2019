import flask
from flask_sqlalchemy import SQLAlchemy
import pyotp

app = flask.Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
random_base = pyotp.random_base32()

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('subscriber_name', db.String(100), nullable=False)
    phone = db.Column('subscriber_phone', db.String(11), nullable=False)
    email = db.Column('subscriber_email', db.String(100), nullable=False)
    confirmed = db.Column('confirmed', db.Boolean(), nullable=False, default=0)