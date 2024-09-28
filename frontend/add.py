from frontend.about import about_ec
from frontend.security import security_bp
from frontend.admin import admin_frontend

def add_frontend(app):
	app.register_blueprint(about_ec)
	app.register_blueprint(security_bp)
	app.register_blueprint(admin_frontend)