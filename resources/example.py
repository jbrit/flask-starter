from functools import wraps
from serializers.example import ExampleSchema
from flask_apispec import marshal_with
from utils import Resource
import models


def allow_only_example(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # check conditions here
        return func(*args, **kwargs)
    return wrapper
    
class Examples(Resource):
    @allow_only_example
    @marshal_with(ExampleSchema(many=True))
    def get(self):
        return models.Example.query.all()

    @marshal_with(ExampleSchema(), code=201)
    def post(self):
        example = models.Example()
        models.db.session.add(example)
        models.db.session.commit()
        return example, 201

