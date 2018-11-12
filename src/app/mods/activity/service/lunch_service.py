#-*- coding:utf-8 -*-

from ....models.activity_model import Activity
from json import dumps

class LunchService(object):
    
    ''' 
    @NAME 午餐业务服务类
    @COMMENT 
    @RETURN_CODE 20010-20020
    '''

    def __init__(self):
        pass

    def create(self,subject,provider_name,*menus,option_max_num,expired_time):
        pass

    def get_by_primary(self,primary_key):
        """Returns a tupel with a dict.
            :format: (code,msg,activity_json)

            :param primary_key:  primary key of the model
        """
        activity = Activity.query.filter_by(id=primary_key)
        if not activity:
            return (20010,"活动不存在")

        return (0,"",activity.__dict__)
        