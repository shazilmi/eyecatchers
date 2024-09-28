from api.security import security_api
from api.admin import admin_api
from api.common import common_api

def add_api(app):
	app.register_blueprint(admin_api)
	app.register_blueprint(security_api)
	app.register_blueprint(common_api)