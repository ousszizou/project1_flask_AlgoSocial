from flask_restful import Resource
from app.models.users import User, users_schema

class UserResource(Resource):
  def get(self):
    users = User.query.all()
    return users_schema.dump(users)