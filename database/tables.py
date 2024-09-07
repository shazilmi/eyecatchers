from database.common import db
from flask_security import UserMixin, RoleMixin

class Rolesusers(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, autoincrement = True, primary_key = True)
	username = db.Column(db.String, unique = False)
	email = db.Column(db.String, unique = True)
	password = db.Column(db.String)
	active = db.Column(db.Boolean, nullable = False, default = True)
	fs_uniquifier = db.Column(db.String, unique = True, nullable = False)
	roles = db.relationship('Role', secondary = 'rolesusers', backref = db.backref('users',
																				lazy = 'dynamic'))

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, unique = True, nullable = False)
	description = db.Column(db.String)

class Sponsor(db.Model):
	id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
	name = db.Column(db.String, nullable = False)
	industry = db.Column(db.String, nullable = False)
	approved = db.Column(db.Boolean, default = False)

class Influencer(db.Model):
	id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
	name = db.Column(db.String, nullable = False)
	category = db.Column(db.String, nullable = False)
	niche = db.Column(db.String)
	yt_followers = db.Column(db.Integer)
	ig_followers = db.Column(db.Integer)
	x_followers = db.Column(db.Integer)

class Campaign(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	niche = db.Column(db.String)
	description = db.Column(db.String)
	sponsor = db.Column(db.Integer, db.ForeignKey('sponsor.id'), nullable = False)
	start_date = db.Column(db.Date)
	end_date = db.Column(db.Date)
	budget = db.Column(db.Integer)
	visibility = db.Column(db.String, nullable = False)
	goals = db.Column(db.String)

class Ad_request(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable = False)
	influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'))
	messages = db.Column(db.String)
	requirements = db.Column(db.String)
	payment_amount = db.Column(db.Integer)
	status = db.Column(db.String)

class Flagged(db.Model):
	id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
	reason = db.Column(db.String)