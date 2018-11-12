# coding=utf-8


from flask import Flask, render_template,request,session,redirect
from . import authentication
from .service.login_service import LoginService

@authentication.route('/')
@authentication.route('/login',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template('authentication/login.html')
    else:
        user_name = request.form.get("login_name",None)
        user_password = request.form.get("login_pwd",None)
        access_data = None
        if not user_name:
            access_data = {
                "return_code":201,
                "return_msg":"缺少登录账号"
            }
            return render_template('authentication/login.html',access_data = access_data)
        if not user_password:
            access_data = {
                "return_code":202,
                "return_msg":"缺少登录密码"
            }
            return render_template('authentication/login.html',access_data = access_data)

        #验证登录信息
        login = LoginService()
        check_result = login.check_login_info(user_name,user_password)
        access_data = {
            "return_code":check_result[0],
            "return_msg":check_result[1]
        }
        
        if check_result[0] != 0:
            return render_template('authentication/login.html',access_data = access_data)
        else:
            user_session_data = {
                "id":check_result[2],
                "user_real_name":check_result[3]
            }
            session["user_session_data"] = user_session_data
            session.permanent = True
            return "<script>location.href='/dashboard/index';</script>"

@authentication.route('/logout')
def logout():
    session.clear()
    return redirect('/login')