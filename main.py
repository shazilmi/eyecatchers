# Importing necessary packages.
from flask import Flask
from initial import initial

# Creating Flask app.
app = Flask(__name__)

# Configuring Flask app.
initial(app)

# Basic route.
@app.route('/', methods = ['GET'])
def home():
	return "Home"

# Running the app.
if __name__ == '__main__':
	app.run(debug = True) 