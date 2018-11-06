# coding=utf-8


from flask import Flask, render_template,session
from . import activity


@activity.route('/activity/detail/<int:activity_id>')
@activity.route('/activity/detail/<string:activity_date>')
def get_detail(activity_id=None,activity_date=None):
    view_data = {
        "title":"详情",
        "current_user":session["user_session_data"],
        "menu_items": ["红烧肉盖饭","鱼香肉丝盖饭","西红烧炒鸡蛋盖饭","扬州炒饭"]
    }
    return render_template('activity/view.html',view_data = view_data)