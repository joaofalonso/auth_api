from db import db
from model.user import User
from repository.user import save, get_user_by_name_or_email, get_user_by_id
from resources.exception.resource_exception import ResourceException

def create(data):
    user = User(**data)
    if(get_user_by_name_or_email(user.name, user.email) is None):
        save(user)
    else:
        raise ResourceException('A user with the same name or email already exists')       
    
def authenticate(data):
    login = data['login']
    db_user = get_user_by_name_or_email(login, login)

    if db_user and (data['pswd'] == db_user.pswd):
        return db_user
    else:
        raise ResourceException('Invalid user and\or password')

def get_by_name_or_email(user_name, user_email):
    return get_user_by_name_or_email(user_name, user_email)

def get_by_id(id):
    return get_user_by_id(id)