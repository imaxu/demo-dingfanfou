# coding=utf-8

from flask import Blueprint,request,session

activity = Blueprint('activity', __name__)

from . import views