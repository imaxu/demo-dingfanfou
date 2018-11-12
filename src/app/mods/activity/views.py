# coding=utf-8


from flask import Flask,session,g
from . import activity
from ..authentication import require_login_session
from ...mods import ViewHolder,render_temp
from .service.lunch_service import LunchService

@activity.route('/activity/detail/<int:activity_id>')
@activity.route('/activity/detail/<string:activity_date>')
@require_login_session
def get_detail(activity_id=None,activity_date=None):

    options = []
    if activity_id:
        lunch = LunchService()
        activity = lunch.get_by_primary(activity_id)
        if activity[0] == 0:
            options = ["红烧肉盖饭","鱼香肉丝盖饭","西红烧炒鸡蛋盖饭","扬州炒饭"]

    ViewHolder["page"] = { 
        "title":"主面板",
        "menu_items":options
    }
    return render_temp('activity/view.html' , view_data = ViewHolder)


@require_login_session
@activity.route('/activity/list/<string:activity_type>')
@activity.route('/activity/list')
def get_list(activity_type=None):

    mapping = {
        "lunch":{
            "name":"午餐",
            "query":None
        }
    }
    ViewHolder["page"] = { 
        "title":mapping[activity_type]["name"],
        "lunch":{
            "total":50,
            "items":[]
        }
    }
    return render_temp('activity/list.html' , view_data = ViewHolder)


@require_login_session
@activity.route('/activity/create/<string:activity_type>')
def create(activity_type=None):
    ViewHolder["page"] = { 
        "title":"发布午餐",
        "lunch":{
            "total":50,
            "items":[]
        }
    }
    return render_temp('activity/create.html')
