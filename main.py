# Importing necessary packages.
from flask import Flask, render_template
from initial import initial
from flask_security import current_user

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

# Basic route.
@app.route('/', methods = ['GET'])
def home():
	if current_user.is_authenticated:
		return render_template('home.html', logged_in = True)
	return render_template('home.html', logged_in = False)

# Running the app.
if __name__ == '__main__':
	app.run(debug = True) 