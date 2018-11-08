# coding=utf-8


from flask import Flask, render_template,request,session,redirect
from . import authentication
from ...models.user_model import User

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
        user = User.query.filter_by(user_name=user_name).first()
        if not user:
            access_data = {
                "return_code":401,
                "return_msg":"账户不正确或者不存在"
            }
            return render_template('authentication/login.html',access_data = access_data)
        if user.user_password != user_password:
            access_data = {
                "return_code":402,
                "return_msg":"账户密码不正确"
            }
            return render_template('authentication/login.html',access_data = access_data)                      

        user_session_data = {
            "id":user.id,
            "user_real_name":user.user_real_name
        }
        session["user_session_data"] = user_session_data
        session.permanent = True
        return "<script>location.href='/dashboard/index';</script>"

@authentication.route('/logout')
def logout():
    session.clear()
    return redirect('/login')