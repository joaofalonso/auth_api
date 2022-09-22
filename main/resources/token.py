import jwt
import resources.user as user_rsc
from datetime import  datetime as dt, timedelta 

secret_key = ""
algorithm = ""

dt_format = '%Y%m%d%H%M%S'
    
def create_token(payload):
    user = user_rsc.authenticate(payload)
    exp_limit = timedelta(hours=2)
    exp_date = dt.now() + exp_limit

    jwt_payload = {
        'sub' : user.id,
        'iss' : user.name,
        'exp' : int(exp_date.strftime(dt_format))
    }

    return token_encode(jwt_payload)


def validate_token(token):
    jwt_payload = token_decode(token)
    user_id = jwt_payload['sub']
    user = user_rsc.get_by_id(user_id)
    token_exp= dt.strptime(str(jwt_payload['exp']), dt_format)

    return user and user.name == jwt_payload['iss'] and  token_exp >= dt.now()

def token_encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def token_decode(token):
    return jwt.decode(token, secret_key, algorithms=[algorithm])
    