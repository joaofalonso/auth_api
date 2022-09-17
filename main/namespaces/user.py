from api import api 
from flask_restx import Resource
from resources.user import create_user
import logging

ns = api.namespace('user', 'User services')


@ns.route('')
class User(Resource):

    def post(self):
        return create_user(api.payload)
