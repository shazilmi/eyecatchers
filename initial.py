 # Importing necessary packages.
from application.config import AppConfig
from flask_security import Security
from werkzeug.security import generate_password_hash
import os
from application.sec import datastore
from database.common import db
from backend.add import add_backend
#from frontend.add import add_frontend
from flask_cors import CORS
import flask_excel as excel
from application.cache import cache

# Function to configure the Flask app, initialize Api object, create datastore, initialize 
# SQLAlchemy object, set up Flask-security, create tables. The tables are populated with the three
# possible roles if none are found. Admin user is also created if not found.
def initial(app):
	app.config.from_object(AppConfig)
	app.security = Security(app, datastore)
	CORS(app)
	excel.init_excel(app)
	db.init_app(app)
	cache.init_app(app)
	with app.app_context():
		db.create_all()
		datastore.find_or_create_role(name = "admin",
									description = "Admin has control over accepting new sponsors,can view stats.")
		datastore.find_or_create_role(name = "sponsor",
								description = "Sponsors can create campaigns and ad requests. They can search for influencers.")
		datastore.find_or_create_role(name = "influencer",
								description = "Influencers can search for ad requests, and can accept or reject ad requests sent by sponsors.")
		db.session.commit()
		if not datastore.find_user(email = "eyecatchershead@gmail.com"):
			try:
				password = os.environ['ADMIN_PASS']
			except:
				password = "Oppose!Handbook7!Scrounger"
			datastore.create_user(email = "eyecatchershead@gmail.com", \
							password = generate_password_hash(password), roles = ["admin"])
		db.session.commit()
	add_backend(app)
	#add_frontend(app)