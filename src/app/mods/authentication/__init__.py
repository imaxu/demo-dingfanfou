# coding=utf-8

from flask import Blueprint,session,redirect,g,request

authentication = Blueprint('authentication', __name__)

from . import views


def require_login_session(func):
    def decorator(*args,**kwargs):
        if "user_session_data" not in session:
            return redirect("/login")
        else:
            print("args:",func)
            viewdata = { "current_user": session["user_session_data"] }
            return func(*args,**kwargs,**viewdata)
    return decorator