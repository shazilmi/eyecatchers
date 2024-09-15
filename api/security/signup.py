from flask import Blueprint, request
from application.sec import datastore
from database.common import db
from werkzeug.security import generate_password_hash
from database.tables import Sponsor, Influencer

signup = Blueprint('api/signup', __name__)
@signup.post('/api/signup')
def signup_user():
	data = request.get_json()
	choice = data.get('choice')
	if not choice:
		return {'message' : 'Error. Role not specified.'}
	if choice == 'sponsor':
		if not data.get('email') or not data.get('industry') or\
		 not data.get('password') or not data.get('name'):
			return {'message' : "Error. Required details were not provided."}
		if not datastore.find_user(email = data.get('email')):
			datastore.create_user(email = data.get('email'),\
						  password = generate_password_hash(data.get('password')), roles = ["sponsor"])
			newid = datastore.find_user(email = data.get('email')).id
			newsponsor = Sponsor(id = newid, name = data.get('name'), industry = data.get('industry'),\
						approved = False)
			db.session.add(newsponsor)
			db.session.commit()
			return {"message" : "Sponsor successfully added."}
		else:
			return {'message' : "Error. Email is already in use."}
	if choice == 'influencer':
		if not data.get('email') or not data.get('password') or not data.get('name') or \
		not data.get('category') or not data.get('niche') or not data.get('x') or \
		not data.get('ig') or not data.get('yt'):
			return {"message" : "Error. Required details not provided."}
		if not datastore.find_user(email = data.get('email')):
			datastore.create_user(email = data.get('email'), \
						 password = generate_password_hash(data.get('password')), \
							roles = ["influencer"])
			newid = datastore.find_user(email = data.get('email')).id
			newinfluencer = Influencer(id = newid, name = data.get('email'), \
							  category = data.get('category'), niche = data.get('category'), \
								yt_followers = data.get('yt'), \
									ig_followers = data.get('ig'), \
										x_followers = data.get('x'))
			db.session.add(newinfluencer)
			db.session.commit()
			return {"message" : "Influencer successfully added."}
		else:
			return {"message": "Error. Email is already in use."}
	else:
		return {"message" : "Error. Invalid role specified."}