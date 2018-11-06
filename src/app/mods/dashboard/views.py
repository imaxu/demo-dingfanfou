# coding=utf-8


from flask import Flask, render_template,request,session
from . import dashboard
from ...models.user_model import User

@dashboard.route('/dashboard/index')
def index():
    view_data = {
        "title":"主面板",
        "current_user":session["user_session_data"]
    }
    return render_template('dashboard/index.html',view_data = view_data)