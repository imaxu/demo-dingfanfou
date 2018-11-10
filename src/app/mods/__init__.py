# coding=utf-8



ViewHolder = {
    "current_user":{}, # 当前登录用户基本信息
    "page":{} # 视图页数据

}


def render_temp(filename,**kwargs):
    from flask import render_template
    if "view_data" not in kwargs:
        kwargs["view_data"] = ViewHolder
        
    return render_template(filename,**kwargs)