from db import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    pswd = Column(String)

    def __repr__(self):
        return f'{self.name} {self.email}'
    