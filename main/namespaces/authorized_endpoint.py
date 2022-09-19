from api import api 
from flask_restx import Resource
from resources.auth import auth_request
from resources.exception.resource_exception import ResourceException
import logging
import json

ns = api.namespace('auth', 'Token validation test endpoint')

@ns.route('')
class Auth(Resource):

    
    def get(self):
        try:
            auth_request()
            return 'Worked', 200
        except ResourceException as err:
            logging.error(err)
            return json.dumps({'error': str(err)}), 202
        except BaseException as err:

            logging.error(err)
            return json.dumps({'error': str(err)}), 500