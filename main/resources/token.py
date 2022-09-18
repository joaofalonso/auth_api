import jwt
from resources.user import authenticate_user
from resources.exception.resource_exception import ResourceException

secret_key = ""
algorithm = ""

def token_encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def token_decode(token):
    return jwt.decode(token, secret_key, algorithms=[algorithm])

def create_token(payload):
    if(authenticate_user(payload)):
        return token_encode(payload)
    else:
        raise Exception('Invalid user and\or password')

def validate_token(token):
    return authenticate_user(token_decode(token))