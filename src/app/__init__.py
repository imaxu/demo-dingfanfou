# coding=utf-8

from flask import Flask

def create_app():
    
    ''' create app from config  '''

    app = Flask(__name__, static_folder = "./templates/static")

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    
    from .mods.activity import activity as activity_blueprint
    app.register_blueprint(activity_blueprint)

    return app


def main():
    app = create_app()
    print(app)


if __name__ == '__main__':
    main()