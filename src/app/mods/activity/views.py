# coding=utf-8


from flask import Flask, render_template
from . import activity


@activity.route('/activity')
def index(path=None):
    return render_template('activity/view.html')