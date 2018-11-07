# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

''' databse setting  '''

db_mode = 'mysql+pymysql'
db_user = 'root'
db_pass = 'ZNNXDKdUIrKmVAYU3TZg4Z4ofL5ckwZs'
db_host = '47.105.38.57'
db_port = '3306'
db_name = 'dingfandb'

db = SQLAlchemy()

def create_app():
    
    ''' create app from config  '''

    app = Flask(__name__, static_folder = "./templates/static")

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True

    #配置 session
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
    app.config['SECRET_KEY'] = "iUuUnRvtznaNBrFtRtFxCkvGn8YmknVC"

    # 数据库配置及初始化
    app.config['SQLALCHEMY_DATABASE_URI'] = \
    '%s://%s:%s@%s:%s/%s' % (db_mode, db_user, db_pass, db_host, db_port, db_name)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)    
    
    from .mods.activity import activity as activity_blueprint
    app.register_blueprint(activity_blueprint)

    from .mods.authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    from .mods.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    return app


def main():
    app = create_app()
    print(app)


if __name__ == '__main__':
    main()