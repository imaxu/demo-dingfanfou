# coding=utf-8


from flask import Flask, render_template,request,session,g
from . import dashboard
from ...models.user_model import User
from ..authentication import require_login_session
from ...mods import ViewHolder

@dashboard.route('/dashboard/index')
@require_login_session
def index():
    ViewHolder["page"] = { "title":"主面板" }
    return render_template('dashboard/index.html', view_data = ViewHolder)