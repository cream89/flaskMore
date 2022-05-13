"""
 File       : app.py
 Time       : 2022/5/13 13:38
 Author     : 黄大彬
 version    : python 3.7.4
"""

from  config.settings import *
from  exts.db import db
from  flask_restful import  Resource
from flask import  Flask
from  apps.user.view import user_blue
from  apps.order.view import  order_blue



def  create_app():

    app=Flask(__name__)
    app.config.from_object(setting)
    db.init_app(app)
    app.register_blueprint(user_blue,url_prefix='/api/user') #会覆盖创建时的url_prefix
    app.register_blueprint(order_blue)   #url_prefix可以在注册蓝图或者是创建蓝图时，注册蓝图时重复写，

    return app