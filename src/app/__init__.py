# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

''' databse setting  '''

db_mode = 'mysql+pymysql'
db_user = 'root'
db_pass = 'ABc@#61^$&@3*(#2Ce>X'
db_host = '192.168.0.20'
db_port = '3306'
db_name = 'dingfandb'

db = SQLAlchemy()

def create_app():
    
    ''' create app from config  '''

    app = Flask(__name__, static_folder = "./templates/static")

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True

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