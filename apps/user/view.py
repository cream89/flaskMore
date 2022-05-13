"""
 File       : view.py
 Time       : 2022/5/13 13:39
 Author     : 黄大彬
 version    : python 3.7.4
"""

from flask  import  Blueprint,request

user_blue=Blueprint('user',__name__)
from .model import *




@user_blue.route('/list',methods=['GET'])
def userList():

    return  'user ist'

@user_blue.route('/list2',methods=['GET'])
def userList1():

    a=request.args.get('a')    #参数获取
    return  a

@user_blue.route('/list3',methods=['POST'])
def userList2():

    username=request.form.get('username')    #参数获取,表单提交
    password = request.form.get('password')
    return  {'username':username,'password':password}


@user_blue.route('/list4',methods=['POST'])
def userList3():

    #res=request.get_data() 获取原始数据 ，byte类型

    username=request.get_json()['username']   #参数获取，json提交
    password = request.json.get('password')
    return  {'username':username,'password':password}