# coding=utf-8

from .. import db
from . import get_date

class Provider(db.Model):

    __tablename__ = 'provider'

    id = db.Column(db.Integer,primary_key=True)
    provider_name = db.Column(db.String(64))
    intro = db.Column(db.String(512))
    address = db.Column(db.String(128))

    def __repr__(self):
        return '<Provider %r >' % self.id