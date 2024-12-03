from flask import Blueprint, request, jsonify
from application.sec import datastore
from werkzeug.security import check_password_hash, generate_password_hash
from flask_security import login_user, auth_required, logout_user
from database.common import db
from database.tables import Sponsor, Influencer
from email_validator import validate_email, EmailNotValidError
from application.cache import cache


security_backend = Blueprint('securitybackend', __name__)

@security_backend.post('/backend/login')
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
		login_user(user)
		return jsonify({'token' : user.get_auth_token(), 'role' : user.roles[0].name,
				  'id' : user.id})
	else:
		return jsonify({'message' : "Error. Invalid login credentials."})
	
@security_backend.post('/backend/logout')
@auth_required('token')
def logout():
	logout_user()
	return jsonify({'message' : "Successfully logged out."})

@security_backend.post('/backend/signup')
def signup_user():
	data = request.get_json()
	choice = data.get('choice')
	if not choice:
		return {'message' : 'Error. Role not specified.'}
	if choice == 'sponsor':
		if not data.get('email') or not data.get('industry') or\
		 not data.get('password') or not data.get('name'):
			print(data)
			return {'message' : "Error. Required details were not provided."}
		try:
			emailinfo = validate_email(data.get('email'), check_deliverability= True)
			email = emailinfo.normalized
		except EmailNotValidError as e:
			message = "Error. " + str(e)
			return {'message' : message}
		if not datastore.find_user(email = email):
			datastore.create_user(email = email,\
						  password = generate_password_hash(data.get('password')), roles = ["sponsor"])
			newid = datastore.find_user(email = email).id
			newsponsor = Sponsor(id = newid, name = data.get('name'), industry = data.get('industry'),\
						approved = False)
			db.session.add(newsponsor)
			db.session.commit()
			return {"success" : "Sponsor successfully added."}
		else:
			return {'message' : "Error. Email is already in use."}
	if choice == 'influencer':
		if not data.get('email') or not data.get('password') or not data.get('name') or \
		not data.get('category') or not data.get('niche') or not data.get('x') or \
		not data.get('ig') or not data.get('yt'):
			return {"message" : "Error. Required details not provided."}
		try:
			emailinfo = validate_email(data.get('email'), check_deliverability= True)
			email = emailinfo.normalized
		except EmailNotValidError as e:
			message = "Error. " + str(e)
			return {'message' : message}
		if not datastore.find_user(email = email):
			datastore.create_user(email = email, \
						 password = generate_password_hash(data.get('password')), \
							roles = ["influencer"])
			newid = datastore.find_user(email = email).id
			newinfluencer = Influencer(id = newid, name = data.get('name'), \
							  category = data.get('category'), niche = data.get('niche'), \
								yt_followers = data.get('yt'), \
									ig_followers = data.get('ig'), \
										x_followers = data.get('x'))
			db.session.add(newinfluencer)
			db.session.commit()
			return {"success" : "Influencer successfully added."}
		else:
			return {"message": "Error. Email is already in use."}
	else:
		return {"message" : "Error. Invalid role specified."}