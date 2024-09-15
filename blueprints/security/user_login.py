from flask import Blueprint, request, render_template, jsonify, redirect, make_response
from flask_security import login_user, current_user
from database.tables import User, Role
from database.common import db
from application.sec import datastore
from werkzeug.security import check_password_hash

security = Blueprint('user-login', __name__)
@security.route('/user-login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('security/login_user.html')
	if request.method == 'POST':
		email = request.form['email']
		if not email:
			return 'Invalid login credentials'
		user = datastore.find_user(email = email)
		if not user:
			return 'Invalid login credentials'
		if check_password_hash(user.password, request.form['password']):
			login_user(user)
			token = user.get_auth_token()
			print(token)
			return token
			'''response = make_response(redirect('admindash'))
			response.headers['a_token'] = token
			return response'''
		else:
			return "Error"