# coding=utf-8

from flask import Blueprint,request,session,g

activity = Blueprint('activity', __name__)

from . import views

@activity.before_request
def on_before_request():
    pass