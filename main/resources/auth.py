import logging
from flask import request
from resources.exception.resource_exception import ResourceException
from resources.token import validate_token

def auth_request():
    token = request.headers.get('token')
    if(token):
        is_valid = validate_token(token)
        if not is_valid:
            raise ResourceException('Invalid token')
    else:
        raise ResourceException('No token found')

