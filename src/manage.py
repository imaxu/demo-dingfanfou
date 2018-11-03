# coding=utf-8

from app import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)


def main():
    manager.run()

if __name__ == '__main__':
    main()