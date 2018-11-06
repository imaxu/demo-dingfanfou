# coding=utf-8


from flask import Flask, render_template,request,session
from . import dashboard
from ...models.user_model import User

@dashboard.route('/dashboard/index')
def index():
    return render_template('dashboard/index.html')