"""
 File       : settings.py
 Time       : 2022/5/13 13:45
 Author     : 黄大彬
 version    : python 3.7.4
"""


class  Base:
    pass

class  Dev(Base):

    ENV='development'
    FLASK_DEBUG=True
    db_host = 'localhost'
    db_port = 3306
    db_name = 'qrcode'
    db_username = 'root'
    db_password = 'root'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (db_username, db_password, db_host, db_port, db_name)
    # redis信息
    redis_host = ''
    redis_port = ''
    redis_name = ''
    redis_password = ''


setting=Dev