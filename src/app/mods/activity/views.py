# coding=utf-8


from flask import Flask, render_template,session
from . import activity


@activity.route('/activity/detail/<int:activity_id>')
def get_detail(activity_id=None):
    view_data = {
        "title":"",
        "current_user":session["user_session_data"],
        "menu_items": ["红烧肉盖饭","鱼香肉丝盖饭","西红烧炒鸡蛋盖饭","扬州炒饭"]
    }
    return render_template('activity/view.html',view_data = view_data)