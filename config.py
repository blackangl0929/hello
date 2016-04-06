import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'K60855D593F732ec push K21459a4868B9A7E'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
	                          'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
	                          'sqlite:///' + os.path.join(basedir,'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
	                          'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,
	'default' : ProductionConfig
}