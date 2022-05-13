from apps.app import create_app
from flask_script import Manager
from flask_migrate import  Migrate,MigrateCommand
from exts.db import db


#导入model
from apps.order.model import *
from apps.user.model import *


app=create_app()
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
