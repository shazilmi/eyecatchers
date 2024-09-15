from flask import Blueprint, request, jsonify
from application.sec import datastore
from werkzeug.security import check_password_hash

login = Blueprint('api/login', __name__)
@login.post('/api/login')
def user_login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	if not email:
		return {'message' : "Error. Email not provided."}
	if not password:
		return {'message' : "Error. Password not provided."}
	user = datastore.find_user(email = email)
	if not user:
		return {'message' : "Error. Invalid login credentials."}
	if check_password_hash(user.password, password):
		return jsonify({'token' : user.get_auth_token()})