"""
 File       : view.py
 Time       : 2022/5/13 13:39
 Author     : 黄大彬
 version    : python 3.7.4
"""

from flask  import  Blueprint

order_blue=Blueprint('order',__name__, url_prefix='/order')



@order_blue.route('/list',methods=['GET'])
def  orderList():

    return 'order list'

