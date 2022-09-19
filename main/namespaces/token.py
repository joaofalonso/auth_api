from api import api
from flask_restx import Resource
from resources.token import create_token
import json
import logging
from resources.exception.resource_exception import ResourceException

ns = api.namespace('token', 'Manage JWT token')

@ns.route('')

class Token(Resource):

    @ns.doc('Validate user data and returns a JWT token when it\'s valid')
    def get(self):
        try:
            return json.dumps({'token' : create_token(api.payload)}), 200
        except ResourceException as err:
            logging.error(err)
            return json.dumps({'error': str(err)}), 202
        except BaseException as err:
            logging.error(err)
            return json.dumps({'error': str(err)}), 500

