from . import db, ma
from flask_login import UserMixin

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy=True)

class UserSchema(ma.Schema):
  class Meta:
    fields = ['email','username']

user_schema = UserSchema()
users_schema = UserSchema(many=True)