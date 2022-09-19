import logging
from flask import request
from resources.exception.resource_exception import ResourceException
from resources.token import validate_token

def auth_request():
    token = request.headers.get('token')
    if(token):
        validate_token(token)
    else:
        raise ResourceException('No token found')

