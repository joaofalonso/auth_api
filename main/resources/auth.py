import logging
from flask import request
from resources.token import validate_token

def auth_request():
    try:
        token = request.headers.get('token')
        validate_token(token)
    except Exception as err:
        raise err
