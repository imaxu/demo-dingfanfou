# coding=utf-8

from .. import db
from . import get_date

class ActivityComment(db.Model):

    __tablename__ = 'activity_comment'

    id = db.Column(db.Integer,primary_key=True)
    activity_id = db.Column(db.Integer,db.ForeignKey('activity.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user_real_name = db.Column(db.String(32))
    user_activity_options = db.Column(db.Text)
    subject = db.Column(db.String(128))
    content = db.Column(db.db.String(256))
    create_time = db.Column(db.DateTime,default=get_date)
    stars = db.Column(db.Integer)

    def __repr__(self):
        return '<ActivityComment %r >' % self.id