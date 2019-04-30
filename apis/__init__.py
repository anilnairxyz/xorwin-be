from flask_restplus import Api
from .numeric_codes_api import api as numeric_codes

api = Api(
    title='My Title',
    version='1.0',
    description='A description'
)

api.add_namespace(numeric_codes, path='/numeric_codes')
