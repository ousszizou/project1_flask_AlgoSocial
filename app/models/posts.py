from . import db
from datetime import datetime

class Post(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
