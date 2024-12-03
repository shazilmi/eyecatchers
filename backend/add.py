from backend.security import security_backend
from backend.admin import admin_backend
from backend.sponsor import sponsor_backend
from backend.influencer import influencer_backend

def add_backend(app):
	app.register_blueprint(security_backend)
	app.register_blueprint(admin_backend)
	app.register_blueprint(sponsor_backend)
	app.register_blueprint(influencer_backend)