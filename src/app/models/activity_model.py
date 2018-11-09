# coding=utf-8

from .. import db
from . import get_date

class Activity(db.Model):

    __tablename__ = 'activity'

    id = db.Column(db.Integer,primary_key=True)
    provider_id = db.Column(db.Integer,db.ForeignKey('provider.id'))
    activity_name = db.Column(db.String(64))
    max_selection = db.Column(db.Integer)
    options = db.Column(db.Text)
    create_time = db.Column(db.DateTime,default=get_date)
    expired_time = db.Column(db.DateTime,default=get_date)
    last_update_tiime = db.Column(db.DateTime,default=get_date)
    state = db.Column(db.Integer)

    def __repr__(self):
        return '<Activity %r >' % self.id