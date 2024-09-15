from flask import Blueprint, render_template, request
from flask_security import roles_required
from database.tables import Influencer
from database.common import db


search_influencers = Blueprint('search_influencer', __name__)
@search_influencers.route('/search_influencer', methods = ['GET', 'POST'])
@roles_required('sponsor')
def search_influencer():
	if request.method == 'GET':
		return render_template('sponsor/search_influencer.html')
	if request.method == 'POST':
		criteria = request.form['criteria']
		value = request.form['value']
		if criteria == 'name':
			results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.x_followers, Influencer.ig_followers).filter(name = value)).all()
		elif criteria == 'category':
			results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.x_followers, Influencer.ig_followers).filter(category = value)).all()
		elif criteria == 'niche':
			results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.x_followers, Influencer.ig_followers).filter(niche = value)).all()
		elif criteria == 'yt':
			results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.x_followers, Influencer.ig_followers).filter(Influencer.yt_followers > int(value))).all()
		elif criteria == 'ig':
			results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.x_followers, Influencer.ig_followers).filter(Influencer.ig_followers > int(value))).all()
		elif criteria == 'x':
			results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.x_followers, Influencer.ig_followers).filter(Influencer.x_followers > int(value))).all()
		print(results)
		return 'results'