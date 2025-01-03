# Importing necessary packages.
import os

# Necessary configuration specifications.
class AppConfig():
	SQLALCHEMY_DATABASE_URI = "sqlite:///../database/eyecatchers.db/"
	DEBUG = True
	SECURITY_PASSWORD_HASH = "bcrypt"
	try:
		SECRET_KEY = os.environ['SECRET_KEY']
		SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']
	except:
		SECRET_KEY = 'Confiding!Bucked0!Width'
		SECURITY_PASSWORD_SALT = 'PF&oRX9oTbQcRD4'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	WTF_CSRF_ENABLED = False
	SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
	SECURITY_EMAIL_SENDER = 'eyecatchershead@gmail.com'
	#SECURITY_REGISTER_USER_TEMPLATE = ''
	#SECURITY_POST_REGISTER_VIEW = ''
	#SECURITY_POST_CHANGE_VIEW = ''
	#SECURITY_CHANGE_PASSWORD_TEMPLATE = ''
	#SECURITY_POST_LOGIN_VIEW = ''
	#SECURITY_POST_LOGOUT_VIEW = ''
	#SECURITY_UNAUTHORIZED_VIEW = ''
	SECURITY_LOGIN_USER_TEMPLATE = 'security/login.html'
	#SECURITY_RESET_PASSWORD_TEMPLATE = ''
	#SECURITY_FORGOT_PASSWORD_TEMPLATE = ''
	#SECURITY_POST_RESET_VIEW = ''
	RESULT_BACKEND = os.environ['SOMETHING']
	BROKER_URL = os.environ['CELERY_BROKER_URL']
	BROKER_CONNECTION_RETRY_ON_STARTUP = True
	TIMEZONE = "Asia/Kolkata"
	CELERY_TASK_SERIALIZER = "pickle"
	CELERY_RESULT_SERIALIZER = "pickle"
	CELERY_ACCEPT_CONTENT = ["pickle"]
	SMTP_SERVER = "localhost"
	SMTP_PORT = 1025
	#SENDER_EMAIL = os.environ['SENDER_EMAIL']
	#SENDER_PASSWORD = os.environ['SENDER_PASSWORD']
	CACHE_TYPE = "RedisCache"
	CACHE_REDIS_HOST = "localhost"
	CACHE_REDIS_PORT = 6379
	CACHE_REDIS_DB = 3
	CACHE_DEFAULT_TIMEOUT = 300