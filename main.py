# Importing necessary packages.
from flask import Flask

# Importing config file.
#from application.config import AppConfig

# Creating Flask app and configuring.
app = Flask(__name__)
#app.config.from_object(AppConfig)

# Importing the LoginManager instance.
#from login.loginmanager import lm
#lm.init_app(app)

# Importing the SQLAlchemy instance.
#from models.common import db
#db.init_app(app)

# Function to create databases and initial admin.
#with app.app_context():
#	create_db()

# Importing Mail instance.
#from application.mail import mail
#mail.init_app(app)

# Adding blueprints.
#from application.blueprints import add_blueprints
#add_blueprints(app)

# Basic route.
@app.route('/', methods = ['GET'])
def home():
	return "Home"

# Running the app.
app.run()