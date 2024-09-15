from api.security.login import login
from api.security.signup import signup
from api.admin.approve_sponsor import approve_sponsor

def add_api(app):
	app.register_blueprint(login)
	app.register_blueprint(signup)
	app.register_blueprint(approve_sponsor)