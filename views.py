from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.example import Examples

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Examples, "/")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Examples, blueprint="api")
# API docs -- end