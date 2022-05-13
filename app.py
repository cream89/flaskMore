from apps.app import create_app
from flask_script import Manager
from exts.db import db

app=create_app()
manager=Manager(app)


if __name__ == '__main__':
    manager.run()
