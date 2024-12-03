from application.sec import datastore
from database.common import db
from database.tables import User, Role, Rolesusers, Sponsor, Influencer, Ad_request, Campaign, Interest
from sqlalchemy import text
from flask import jsonify

def get_pending_approvals():
	thelist = db.session.execute(db.select(Sponsor.id, Sponsor.name, Sponsor.industry).filter_by(approved = False)).all()
	alist = []
	for i in thelist:
		alist.append([int(i[0]), i[1], i[2]])
	return alist

def get_sponsor_id():
	thelist = db.session.execute(db.select(Sponsor.id)).all()
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
	thelist = jsonify({"users" : users,
				   "sponsors" : sponsors,
				   "influencers" : influencers,
				   "unapproved" : unapproved,
				   "campaigns" : campaigns,
				   "ads" : ad_requests,
				   "flagged" : flagged,
				   "public_campaigns" : public_campaigns})
	return thelist

def get_campaign(user_id):
	thelist = db.session.execute(db.select(Campaign.id, Campaign.description, Campaign.name, Campaign.niche, Campaign.budget, Campaign.goals, Campaign.start_date, Campaign.end_date, Campaign.visibility).filter_by(sponsor = user_id)).all()
	return thelist

def get_campaign_user(user_id):
	details = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter_by(sponsor = user_id)).scalars()
	return details

def get_campaign_details(campaign_id):
	details = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter_by(id = campaign_id)).one()
	return details

def get_ad(user_id):
	campaigns = db.session.execute(db.select(Campaign.id).filter_by(sponsor = user_id)).scalars()
	thelist = []
	for i in campaigns:
		ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status).filter_by(campaign_id = i)).all()
		for i in ads:
			thelist.append(i)
	return thelist

def get_ad_by_influencer(influencer_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.influencer_id == influencer_id) & (Ad_request.status == 'pending') & (Ad_request.made_by == 'sponsor'))).all()
	thelist = []
	for i in ads:
		sponsor = db.session.execute(db.select(Campaign.sponsor).filter(Campaign.id == i[1])).one()[0]
		sponsorname = db.session.execute(db.select(Sponsor.name).filter_by(id = sponsor)).one()[0]
		alist = []
		for j in i:
			alist.append(j)
		alist.append(sponsor)
		alist.append(sponsorname)
		thelist.append(alist)
	return thelist

def get_ad_made_by_influencer(influencer_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.influencer_id == influencer_id) & (Ad_request.made_by == 'influencer') & (Ad_request.status == 'pending'))).all()
	thelist = []
	for i in ads:
		sponsor = db.session.execute(db.select(Campaign.sponsor).filter(Campaign.id == i[1])).one()[0]
		sponsorname = db.session.execute(db.select(Sponsor.name).filter_by(id = sponsor)).one()[0]
		alist = []
		for j in i:
			alist.append(j)
		alist.append(sponsor)
		alist.append(sponsorname)
		thelist.append(alist)
	return thelist

def get_ad_accepted_by_influencer(influencer_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.influencer_id == influencer_id) & (Ad_request.status == 'accepted'))).all()
	thelist = []
	for i in ads:
		sponsor = db.session.execute(db.select(Campaign.sponsor).filter(Campaign.id == i[1])).one()[0]
		sponsorname = db.session.execute(db.select(Sponsor.name).filter_by(id = sponsor)).one()[0]
		alist = []
		for j in i:
			alist.append(j)
		alist.append(sponsor)
		alist.append(sponsorname)
		thelist.append(alist)
	return thelist

def get_ad_rejected_by_influencer(influencer_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.influencer_id == influencer_id) & (Ad_request.status == 'rejected'))).all()
	thelist = []
	for i in ads:
		sponsor = db.session.execute(db.select(Campaign.sponsor).filter(Campaign.id == i[1])).one()[0]
		sponsorname = db.session.execute(db.select(Sponsor.name).filter_by(id = sponsor)).one()[0]
		alist = []
		for j in i:
			alist.append(j)
		alist.append(sponsor)
		alist.append(sponsorname)
		thelist.append(alist)
	return thelist

def get_ad_by_campaign(campaign_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.campaign_id == campaign_id) & (Ad_request.status == 'pending') & (Ad_request.made_by == 'sponsor'))).all()
	thelist = []
	for i in ads:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def get_interest_by_campaign(campaign_id):
	interest = db.session.execute(db.select(Interest.id, Interest.influencer_id).filter_by(campaign_id = campaign_id)).all()
	thelist = []
	for i in interest:
		influencer_name = db.session.execute(db.select(Influencer.name).filter_by(id = i[1])).one()[0]
		alist = []
		for j in i:
			alist.append(j)
		alist.append(influencer_name)
		thelist.append(alist)
	return thelist

def get_pending_ad_by_campaign(campaign_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.campaign_id == campaign_id) & (Ad_request.made_by == 'influencer') & (Ad_request.status == 'pending'))).all()
	thelist = []
	for i in ads:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def get_accepted_ad_by_campaign(campaign_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.campaign_id == campaign_id) & (Ad_request.status == 'accepted'))).all()
	thelist = []
	for i in ads:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist	

def get_rejected_ad_by_campaign(campaign_id):
	ads = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status, Ad_request.influencer_id, Ad_request.made_by).filter((Ad_request.campaign_id == campaign_id) & (Ad_request.status == 'rejected'))).all()
	thelist = []
	for i in ads:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def get_ad_details(ad_id):
	details = db.session.execute(db.select(Ad_request.id, Ad_request.campaign_id, Ad_request.influencer_id, Ad_request.requirements, Ad_request.payment_amount, Ad_request.status).filter_by(id = ad_id)).one()
	return details

def get_influencers():
	influencers = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.ig_followers, Influencer.x_followers)).all()
	thelist = []
	for i in influencers:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def get_basic_sponsor(id):
	basics = db.session.execute(db.select(Sponsor.name, Sponsor.industry).filter_by(id = id)).one()
	basics = [basics[0], basics[1]]
	campaigns = get_campaign(id)
	thecampaigns = []
	for i in campaigns:
		alist = []
		for j in i:
			alist.append(j)
		thecampaigns.append(alist)
	ads = get_ad(id)
	theads = []
	for j in ads:
		theads.append(j)
	return {
		"basic" : basics,
		"campaigns" : thecampaigns,
		#"ads" : theads,
	}

def search_influencer_niche(search_niche):
	results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.ig_followers, Influencer.x_followers).filter(Influencer.niche.contains(search_niche))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_influencer_category(search_category):
	results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.ig_followers, Influencer.x_followers).filter(Influencer.category.contains(search_category))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_influencer_name(search_name):
	results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.ig_followers, Influencer.x_followers).filter(Influencer.name.contains(search_name))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_influencer_followers(search_followers):
	results = db.session.execute(db.select(Influencer.id, Influencer.name, Influencer.category, Influencer.niche, Influencer.yt_followers, Influencer.ig_followers, Influencer.x_followers).filter((Influencer.yt_followers > search_followers) | (Influencer.ig_followers > search_followers) | (Influencer.x_followers > search_followers))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_campaign_name(name):
	results = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter((Campaign.visibility == 'public') & (Campaign.name.contains(name)))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_campaign_niche(niche):
	results = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter((Campaign.visibility == 'public') & (Campaign.niche.contains(niche)))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_campaign_description(description):
	results = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter((Campaign.visibility == 'public') & (Campaign.description.contains(description)))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def search_campaign_budget(budget):
	results = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter((Campaign.visibility == 'public') & (Campaign.budget > budget))).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist

def get_public_campaigns():
	results = db.session.execute(db.select(Campaign.id, Campaign.name, Campaign.niche, Campaign.description, Campaign.sponsor, Campaign.start_date, Campaign.end_date, Campaign.budget, Campaign.visibility, Campaign.goals).filter(Campaign.visibility == 'public')).all()
	thelist = []
	for i in results:
		alist = []
		for j in i:
			alist.append(j)
		thelist.append(alist)
	return thelist	

def get_influencer_reminder():
	influencers = db.session.execute(db.select(Ad_request.influencer_id).filter((Ad_request.status == 'pending') & (Ad_request.made_by == 'sponsor'))).all()
	emails = []
	for i in influencers:
		email = db.session.execute(db.select(User.email).filter_by(id = i[0])).one()[0]
		emails.append(email)
	return emails