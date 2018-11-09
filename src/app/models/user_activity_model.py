# coding=utf-8

from .. import db
from . import get_date

class UserActivity(db.Model):

    __tablename__ = 'user_activity'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    activity_id = db.Column(db.Integer,db.ForeignKey('activity.id'))
    options = db.Column(db.Text)
    op_time = db.Column(db.DateTime,default=get_date)

    def __repr__(self):
        return '<UserActivity %r >' % self.id