import os
from . import create_app,db
from models import User,Role
from flask.ext.script import Manager,Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
	manager.run()