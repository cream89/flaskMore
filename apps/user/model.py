"""
 File       : model.py
 Time       : 2022/5/13 13:39
 Author     : 黄大彬
 version    : python 3.7.4
"""

from exts.db import db

class  User(db.Model):

    ___tablename__='user'

    order_id=db.Column(db.Integer,nullable=False)
    order_op=db.Column(db.String,nullable=False)