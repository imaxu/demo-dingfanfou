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
        print(activity)
        if activity[0] == 0:
            ViewHolder["page"] = { 
                "title":"详情",
                "menu_items":activity[2].get("options").split(","),
                "activity_name":activity[2].get("activity_name"),
                "create_time":activity[2].get("create_time"),
                "max_selection":activity[2].get("max_selection")
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
