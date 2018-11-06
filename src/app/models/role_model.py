# coding=utf-8

from .. import db
from . import get_date

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    role_name = db.Column(db.String(32))

    def __repr__(self):
        return '<Role %r >' % self.id