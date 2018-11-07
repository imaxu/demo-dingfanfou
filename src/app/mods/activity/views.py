# coding=utf-8


from flask import Flask, render_template,session,g
from . import activity
from ..authentication import require_login_session


@activity.route('/activity/detail/<int:activity_id>')
@activity.route('/activity/detail/<string:activity_date>')
@require_login_session
def get_detail(activity_id=None,activity_date=None,**viewdata):
    viewdata["page"] = {
        "title":"详情",
        "menu_items": ["红烧肉盖饭","鱼香肉丝盖饭","西红烧炒鸡蛋盖饭","扬州炒饭"]
    }
    return render_template('activity/view.html',view_data = viewdata)


@activity.route('/activity/list/<string:activity_type>')
@activity.route('/activity/list')
@require_login_session
def get_list(activity_type=None,**viewdata):
    viewdata["page"] = {
        "title":"详情"
    }
    return render_template('activity/list.html',view_data = viewdata)


@activity.route('/activity/create/<string:activity_type>')
@require_login_session
def create(activity_type=None):
    return "create_%s" % activity_type
