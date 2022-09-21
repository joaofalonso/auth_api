from sqlalchemy import or_ 
from db import db
from model.user import User
import logging

def save(user):
    if(user.id is None):
        db.session.add(user)
    else:
        db.session.merge(user)
    db.session.commit()

def get_user_by_name_or_email(name, email):
    return db.session.query(User).filter(or_(User.name == name, User.email == email)).first()

def get_user_by_id(id):
    return db.session.query(User).filter(User.id == id).first()
