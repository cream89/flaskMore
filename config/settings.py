"""
 File       : settings.py
 Time       : 2022/5/13 13:45
 Author     : 黄大彬
 version    : python 3.7.4
"""


class  Base:
    pass

class  Dev(Base):

    ENV='production'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    FLASK_DEBUG = False
    #数据库信息
    db_host='11'
    db_port='22'
    db_name='33'
    db_username='44'
    db_password=''
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'


setting=Dev