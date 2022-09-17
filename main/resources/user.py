from db import db
from model.user import User
from repository.user import save, find_user
import logging

def create_user(data):
    user = User(**data)
    if(find_user(user.name, user.email) is None):
        save(user)
    else:
        raise Exception('A user with the same name or email already exists')       
    
def authenticate_user(data):
    login = data['login']
    db_user = find_user(login, login)

    return db_user and (data['pswd'] == db_user.pswd)
