# coding=utf-8

from flask import Blueprint,session,redirect,request,g

authentication = Blueprint('authentication', __name__)

from . import views
from functools import wraps
from ...mods import ViewHolder

def require_login_session(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        if "user_session_data" not in session:
            return redirect("/login")
        else:
            ViewHolder["current_user"] = session["user_session_data"]
            return func(*args,**kwargs)
    return decorator