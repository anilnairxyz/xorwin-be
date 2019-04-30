from flask_restplus import Namespace, Resource, fields
from xorwin.numeric_codes import numeric_codes_question

api = Namespace('numeric_codes', description='Non-verbal reasoning: 4 letter word numeric codes')

numeric_codes = api.model('numericCodes', {
    'problem_type': fields.String(required=True, description='Problem type identifier'),
    'words': fields.List(fields.String, required=True, description='The 4 word list'),
    'codes': fields.List(fields.String, required=True, description='The 3 code list'),
    'query': fields.String(required=True, description='The query word'),
    'result': fields.String(required=True, description='The result code'),
})


@api.route('/')
class NumericCodes(Resource):
    @api.doc('Random numeric code problem')
    @api.marshal_with(numeric_codes)
    def get(self):
        """Generate a random numeric code problem"""
        words, codes, query, result = numeric_codes_question()
        question = {'problem_type': 1,
                    'words': words,
                    'codes': codes,
                    'query': query,
                    'result': result
                    }
        return question
