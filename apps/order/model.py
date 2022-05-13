"""
 File       : model.py
 Time       : 2022/5/13 13:39
 Author     : 黄大彬
 version    : python 3.7.4
"""

from exts.db import db

class  Order(db.Model):

    ___tablename__='order'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.Integer,nullable=False)
    password=db.Column(db.String(20),nullable=False)