# Importing blueprints to be added.
from blueprints.admin.admin_activate_sponsor import adminapprovals
from blueprints.admin.admin_dash import admindashs
from blueprints.security.signup import signups

# Function to register blueprints to app.
def add_blueprints(app):
	app.register_blueprint(admindashs)
	app.register_blueprint(adminapprovals)
	app.register_blueprint(signups)