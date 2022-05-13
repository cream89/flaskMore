"""
 File       : view.py
 Time       : 2022/5/13 13:39
 Author     : 黄大彬
 version    : python 3.7.4
"""

from flask  import  Blueprint

user_blue=Blueprint('user',__name__)



@user_blue.route('/list',methods=['GET'])
def userList():

    return  'user ist'