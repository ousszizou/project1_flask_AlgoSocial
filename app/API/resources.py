from flask_restful import Resource
from app.models.users import User, users_schema
from flask_jwt_extended import jwt_required

class UserResource(Resource):
  @jwt_required
  def get(self):
    users = User.query.all()
    return users_schema.dump(users)