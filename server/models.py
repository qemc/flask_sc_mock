from server import db
from uuid import uuid4
from sqlalchemy.dialects.mysql import LONGTEXT

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    email = db.Column(db.Text(), nullable=False)

class Events(db.Model):
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    starth = db.Column(db.Integer(), nullable = False)
    startm = db.Column(db.Integer(), nullable = False)
    duration = db.Column(db.Integer(), nullable = False)
    week = db.Column(db.Integer(), nullable = False)
    desc = db.Column(db.String(length=800), nullable=False)
    title = db.Column(db.String(length=100), nullable=False)
    day_of_week = db.Column(db.Integer(), nullable = False)

class Todos(db.Model):
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    status = db.Column(db.Boolean, default=False, nullable=False)
    text = db.Column(db.String(length=800), nullable=False)
    week = db.Column(db.Integer(), nullable = False)
    day_of_week = db.Column(db.Integer(), nullable = False)

class Notes(db.Model):
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    title = db.Column(db.String(length=100), nullable=False)
    text = db.Column(db.String(length=800), nullable=False)

# to create db conn: in python terminal import app and db and import all your db models then db.create_all(). If SQL query is shown itself, you ok. if not, try again.

