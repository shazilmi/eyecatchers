# Importing blueprints to be added.
from blueprints.admin.admin_activate_sponsor import adminapprovals
from blueprints.admin.admin_dash import admindashs
from blueprints.security.signup import signups
from blueprints.admin.admin_stats import adminstats
from blueprints.sponsor.create_campaign import create_campaigns
from blueprints.sponsor.update_campaign import update_campaigns
from blueprints.sponsor.delete_campaign import delete_campaigns
from blueprints.sponsor.create_ad import create_ads
from blueprints.sponsor.delete_ad import delete_ads
from blueprints.sponsor.update_ad import update_ads

# Function to register blueprints to app.
def add_blueprints(app):
	app.register_blueprint(admindashs)
	app.register_blueprint(adminapprovals)
	app.register_blueprint(signups)
	app.register_blueprint(adminstats)
	app.register_blueprint(create_campaigns)
	app.register_blueprint(update_campaigns)
	app.register_blueprint(delete_campaigns)
	app.register_blueprint(create_ads)
	app.register_blueprint(delete_ads)
	app.register_blueprint(update_ads)