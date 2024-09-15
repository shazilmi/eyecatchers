from flask import Blueprint, request, render_template
from werkzeug.security import generate_password_hash
from application.sec import datastore
from database.common import db
from database.tables import Sponsor, Influencer

signups = Blueprint('signup', __name__)
@signups.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('security/signup_choice.html')
	if request.method == 'POST':
		try:
			choice = request.form['choice']
			if choice == 'sponsor':
				return render_template('security/signup_sponsor.html')
			elif choice == 'influencer':
				return render_template('security/signup_influencer.html')
		except:
			try:
				industry = request.form['industry']
				if not datastore.find_user(email = request.form['email']):
					datastore.create_user(email = request.form['email'], \
						password = generate_password_hash(request.form['password']), \
								roles = ["sponsor"])
					newid = datastore.find_user(email = request.form['email']).id
					newsponsor = Sponsor(id = newid, name = request.form['name'], \
						industry = industry, approved = False)
					db.session.add(newsponsor)
					db.session.commit()
					return 'Done'
			except:
				if not datastore.find_user(email = request.form['email']):
					datastore.create_user(email = request.form['email'], \
						   password = generate_password_hash(request.form['password']), \
								  roles = ["influencer"])
					newid = datastore.find_user(email = request.form['email']).id
					print(newid)
					newinfluencer = Influencer(id = newid, name = request.form['name'], \
								category = request.form['category'], \
									niche = request.form['niche'],\
										  yt_followers = request.form['yt'],\
											x_followers = request.form['x'], \
											ig_followers = request.form['ig'])
					db.session.add(newinfluencer)
					db.session.commit()
					return 'Done'