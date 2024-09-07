from application.sec import datastore
from database.common import db
from database.tables import User, Role, Rolesusers, Sponsor, Influencer, Ad_request, Campaign, Flagged
from sqlalchemy import text

def get_pending_approvals():
	thelist = db.session.execute(db.select(Sponsor.id, Sponsor.name, Sponsor.industry).filter_by(approved = False)).all()
	return thelist

def get_stats():
	users = int(db.session.execute(text('SELECT COUNT(*) FROM USER;')).one()[0])
	sponsors = int(db.session.execute(text('SELECT COUNT(*) FROM SPONSOR;')).one()[0])
	influencers = int(db.session.execute(text('SELECT COUNT(*) FROM INFLUENCER;')).one()[0])
	unapproved = int(db.session.execute(text('SELECT COUNT(*) FROM SPONSOR WHERE "APPROVED" = FALSE;')).one()[0])
	campaigns = int(db.session.execute(text('SELECT COUNT(*) FROM CAMPAIGN;')).one()[0])
	ad_requests = int(db.session.execute(text('SELECT COUNT(*) FROM AD_REQUEST;')).one()[0])
	flagged = int(db.session.execute(text('SELECT COUNT(*) FROM FLAGGED;')).one()[0])
	public_campaigns = int(db.session.execute(text('SELECT COUNT(*) FROM CAMPAIGN WHERE "VISIBILITY" = "public";')).one()[0])
	thelist = [users, sponsors, influencers, unapproved, campaigns, ad_requests, flagged, public_campaigns]
	return thelist

def get_campaign(user_id):
	thelist = db.session.execute(db.select(Campaign.id, Campaign.description, Campaign.budget, Campaign.goals, Campaign.start_date, Campaign.end_date, Campaign.visibility).filter_by(sponsor = user_id)).all()
	return thelist

def get_campaign_details(campaign_id):
	details = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter_by(id = campaign_id)).one()
	return details