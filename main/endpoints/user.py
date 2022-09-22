from api import api 
from flask_restx import Resource
from resources.user import create
import logging
import json
from resources.exception.resource_exception import ResourceException

ns = api.namespace('user', 'User services')

@ns.route('')
class User(Resource):

    @ns.doc('Create a user')
    def post(self):
        try:
            return create(api.payload), 200
        except ResourceException as err:
            logging.error(err)
            return json.dumps({'error': str(err)}), 202
        except Exception as err:
            logging.error(err)
            return json.dumps({'error': str(err)}), 500



        