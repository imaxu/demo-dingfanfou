# -*- coding:utf-8 -*-

from .. import db

class BaseModel(db.Model):

    __abstract__ = True

    def __init__(self):
        pass

    def to_dict(self):
        self.__dict__.pop("_sa_instance_state",None)
        return self.__dict__