from flask_restful import Api
from . import resources

# create API
api = Api()
api.add_resource(resources.UserResource, '/api/users')