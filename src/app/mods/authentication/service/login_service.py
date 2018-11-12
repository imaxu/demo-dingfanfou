# coding=utf-8

from ....models.user_model import User

class LoginService(object):

    def __init__(self):
        pass

    def check_login_info(self,user_name,user_password):
        #验证登录信息
        user = User.query.filter_by(user_name=user_name).first()
        if not user:
            return (401,"账户不正确或者不存在")
        if user.user_password != user_password:
            return (402,"账户密码不正确")

        return (0,"",user.id,user.user_real_name)