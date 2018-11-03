# coding=utf-8


from flask import Flask, render_template
from . import auth


@auth.route('/', defaults={'path': ''})
@auth.route('/<path:path>')
def index(path=None):
    return render_template('index.html')

