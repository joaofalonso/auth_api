from db import db
from model.user import User
def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    