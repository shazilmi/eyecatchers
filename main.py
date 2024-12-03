# Importing necessary packages.
from flask import Flask, render_template, jsonify
from initial import initial
from flask_security import current_user
from application.workers import celery_init_app
from celery.schedules import crontab
from application.tasks import daily_reminder

# Creating Flask app.
class CustomFlask(Flask):
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
		variable_start_string = '%%',
		variable_end_string = '%%',
	))
app = CustomFlask(__name__)

# Configuring Flask app.
initial(app)
celery_app = celery_init_app(app)

@celery_app.on_after_configure.connect
def send_email(sender, **kwargs):
	sender.add_periodic_task(
		crontab(hour = 19, minute = 30),
		daily_reminder.s(),
	)

# Basic route.
@app.route('/', methods = ['GET'])
def home():
	#if current_user.is_authenticated:
		#return render_template('home.html', logged_in = True)
	#return render_template('home.html', logged_in = False)
	return "Hehehe"

# Running the app.
if __name__ == '__main__':
	app.run(debug = True, port = 8000)