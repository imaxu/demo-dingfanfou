# coding=utf-8

from .. import db
from . import get_date

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    role_id = db.Column(db.Integer)
    user_name = db.Column(db.String(32))
    user_password = db.Column(db.String(64))
    user_real_name = db.Column(db.String(32))
    registration_time = db.Column(db.DateTime,default=get_date)

    def __repr__(self):
        return '<User %r >' % self.id