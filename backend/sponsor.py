from flask import Blueprint, jsonify, request, send_file
from flask_security import auth_required, roles_required, current_user, roles_accepted
from database.tables import Sponsor, Campaign, Ad_request, Influencer
from database.common import db
from database.functions import get_basic_sponsor, get_campaign_details, get_ad_by_campaign, get_influencers, search_influencer_niche, search_influencer_category, search_influencer_followers, search_influencer_name, get_pending_ad_by_campaign, get_interest_by_campaign, get_accepted_ad_by_campaign, get_rejected_ad_by_campaign
from datetime import date
import flask_excel as excel
from application.tasks import create_resource
from celery.result import AsyncResult
from application.cache import cache

sponsor_backend = Blueprint("sponsorbackend", __name__)

@sponsor_backend.post("/backend/sponsor/create_campaign")
@auth_required("token")
@roles_required("sponsor")
def create():
	data = request.get_json()
	if not data.get('sponsor'):
		return {"message" : "Error. ID of sponsor was not provided."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get('sponsor'))).scalar()
	if not sponsor:
		return {"message" : "Error. No such sponsor exists."}
	if not data.get('name') or not data.get('niche') or not data.get('description')\
	or not data.get('start_date') or not data.get('end_date')\
	or not data.get('budget') or not data.get('visibility') or not data.get('goals'):
		return {"message" : "Error. Required details were not provided."}
	if data.get('visibility') not in ['private', 'public']:
		return {"message" : "Error. Invalid visibility for campaign entered."}
	try:
		start = data.get('start_date')
		start_date = date(int(start[0:4]), int(start[5:7]), int(start[8:10]))
		end = data.get('end_date')
		end_date = date(int(end[0:4]), int(end[5:7]), int(end[8:10]))
		newcampaign = Campaign(name = data.get('name'), niche = data.get('niche'),
							description = data.get('description'), start_date = start_date,
							end_date = end_date, budget = data.get('budget'),
							visibility = data.get('visibility'), goals = data.get('goals'),
							sponsor = data.get('sponsor'))
		db.session.add(newcampaign)
		db.session.commit()
		return {"success" : "Campaign created successfully."}
	except:
		return {"message" : "Error. A date-related error or another unknown error occurred."}
	
@sponsor_backend.post('/backend/sponsor/delete_campaign')
@auth_required("token")
@roles_required("sponsor")
def delete():
	data = request.get_json()
	if not data.get('campaign_id'):
		return {"message" : "Error. Campaign to be deleted was not provided."}
	if not data.get('sponsor_id'):
		return {"message" : "Error. Sponsor must send the request to delete campaign."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get("sponsor_id"))).scalar()
	if not sponsor:
		return {"message" : "Error. Invalid sponsor."}
	campaign = db.session.execute(db.select(Campaign).filter_by(id = data.get("campaign_id"))).scalar()
	if not campaign:
		return {"message" : "Error. Invalid campaign."}
	if int(campaign.sponsor) != int(data.get('sponsor_id')):
		return {"message" : "Error. Only the owner can delete a campaign."}
	try:
		db.session.delete(campaign)
		db.session.commit()
		return {"success" : "Campaign was successfully deleted."}
	except:
		return {"message" : "Error. An unknown error was detected."}
	
@sponsor_backend.post("/backend/sponsor/update_campaign")
@auth_required("token")
@roles_required("sponsor")
def update():
	data = request.get_json()
	if not data.get('sponsor'):
		return {"message" : "Error. ID of sponsor was not provided."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get('sponsor'))).scalar()
	if not sponsor:
		return {"message" : "Error. No such sponsor exists."}
	if not data.get('campaign'):
		return {"message" : "Error. Campaign to be updated was not provided."}
	campaign = db.session.execute(db.select(Campaign).filter_by(id = data.get("campaign"))).scalar()
	if not campaign:
		return {"message" : "Error. Invalid campaign."}
	if int(campaign.sponsor) != int(data.get("sponsor")):
		return {"message" : "Error. Only the owner can update the campaign."}
	if not data.get('name') or not data.get('niche') or not data.get('description')\
	or not data.get('start_date') or not data.get('end_date')\
	or not data.get('budget') or not data.get('visibility') or not data.get('goals'):
		return {"message" : "Error. Required details were not provided."}
	if data.get('visibility') not in ['private', 'public']:
		return {"message" : "Error. Invalid visibility for campaign entered."}
	try:
		start = data.get('start_date')
		start_date = date(int(start[0:4]), int(start[5:7]), int(start[8:10]))
		end = data.get('end_date')
		end_date = date(int(end[0:4]), int(end[5:7]), int(end[8:10]))
		campaign.name = data.get('name')
		campaign.niche = data.get('niche')
		campaign.description = data.get('description')
		campaign.visibility = data.get('visibility')
		campaign.budget = data.get('budget')
		campaign.start_date = start_date
		campaign.end_date = end_date
		campaign.goals = data.get('goals')
		db.session.commit()
		return {"success" : "Campaign details were successfully updated."}
	except:
		return {"message" : "Error. An unknown error occurred."}
	
@sponsor_backend.post("/backend/sponsor/create_ad_request")
@auth_required("token")
@roles_required("sponsor")
def create_request():
	data = request.get_json()
	if not data.get('sponsor'):
		return {"message" : "Error. ID of sponsor was not provided."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get('sponsor'))).scalar()
	if not sponsor:
		return {"message" : "Error. No such sponsor exists."}
	if not data.get('campaign'):
		return {"message" : "Error. Campaign for which request is to be made was not provided."}
	campaign = db.session.execute(db.select(Campaign).filter_by(id = data.get("campaign"))).scalar()
	if not campaign:
		return {"message" : "Error. Invalid campaign."}
	if int(campaign.sponsor) != int(data.get("sponsor")):
		return {"message" : "Error. Only the owner of the campaign can make an ad request."}
	if not data.get('influencer_id') or not data.get('requirements')\
	or not data.get('payment_amount'):
		return {"message" : "Error. Required details were not provided."}
	influencer = db.session.execute(db.select(Influencer).filter_by(id = data.get('influencer_id'))).scalar()
	if not influencer:
		return {"message" : "Error. No such influencer was found."}
	try:
		newad = Ad_request(campaign_id = data.get('campaign'),
					influencer_id = data.get('influencer_id'),
					requirements = data.get('requirements'),
					payment_amount = data.get('payment_amount'),
					made_by = 'sponsor',
					status = "pending")
		db.session.add(newad)
		db.session.commit()
		return {"success" : "Ad request was successfully created."}
	except:
		return {"message" : "Error. An unknown error occurred."}
	
@sponsor_backend.post("/backend/sponsor/update_ad_request")
@auth_required("token")
@roles_required("sponsor")
def update_ad():
	data = request.get_json()
	if not data.get('sponsor'):
		return {"message" : "Error. ID of sponsor was not provided."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get('sponsor'))).scalar()
	if not sponsor:
		return {"message" : "Error. No such sponsor exists."}
	if not data.get('ad_id'):
		return {"message" : "Error. Ad request to be updated was not provided."}
	ad_request = db.session.execute(db.select(Ad_request).filter_by(id = data.get('ad_id'))).scalar()
	if not ad_request:
		return {"message" : "Error. Invalid ad request."}
	campaign = db.session.execute(db.select(Campaign).filter_by(id = ad_request.campaign_id)).scalar()
	if not campaign:
		return {"message" : "Error. Invalid campaign."}
	if int(campaign.sponsor) != int(data.get("sponsor")):
		return {"message" : "Error. Only the owner of the campaign can update an ad request."}
	if not data.get('influencer_id') or not data.get('requirements')\
	or not data.get('payment_amount'):
		return {"message" : "Error. Required details were not provided."}
	influencer = db.session.execute(db.select(Influencer).filter_by(id = data.get('influencer_id'))).scalar()
	if not influencer:
		return {"message" : "Error. No such influencer was found."}
	try:
		ad_request.influencer_id = data.get('influencer_id')
		ad_request.requirements = data.get('requirements')
		ad_request.payment_amount = data.get('payment_amount')
		ad_request.made_by = 'sponsor'
		ad_request.status = 'pending'
		db.session.commit()
		return {"success" : "Ad request details were successfully updated."}
	except:
		return {"message" : "Error. An unknown error occurred."}
	

@sponsor_backend.post("/backend/sponsor/delete_ad_request")
@auth_required("token")
@roles_required("sponsor")
def delete_ad():
	data = request.get_json()
	if not data.get('sponsor'):
		return {"message" : "Error. ID of sponsor was not provided."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get('sponsor'))).scalar()
	if not sponsor:
		return {"message" : "Error. No such sponsor exists."}
	if not data.get('ad_id'):
		return {"message" : "Error. Ad request to be deleted was not provided."}
	ad_request = db.session.execute(db.select(Ad_request).filter_by(id = data.get('ad_id'))).scalar()
	if not ad_request:
		return {"message" : "Error. Invalid ad request."}
	campaign = db.session.execute(db.select(Campaign).filter_by(id = ad_request.campaign_id)).scalar()
	if not campaign:
		return {"message" : "Error. Invalid campaign."}
	if int(campaign.sponsor) != int(data.get("sponsor")):
		return {"message" : "Error. Only the owner of the campaign can delete an ad request."}
	try:
		db.session.delete(ad_request)
		db.session.commit()
		return {"success" : "Ad request was successfully deleted."}
	except:
		return {"message" : "Error. An unknown error occurred."}
	
@sponsor_backend.get('/backend/sponsor/sponsor_basic_stats')
@auth_required("token")
@roles_required("sponsor")
#@cache.cached(timeout = 300)
def get_basic_stats():
	basics = get_basic_sponsor(current_user.id)
	return basics

@sponsor_backend.post('/backend/sponsor/campaign_details')
@auth_required("token")
@roles_required("sponsor")
#@cache.cached(timeout = 300)
def get_campaign():
	data = request.get_json()
	if not data.get("id"):
		return {"message" : "Error. Campaign id was not provided."}
	thelist = get_campaign_details(data.get("id"))
	alist = []
	for i in thelist:
		alist.append(i)
	return alist

@sponsor_backend.post('/backend/sponsor/ad_details')
@auth_required("token")
@roles_required("sponsor")
def get_ad():
	data = request.get_json()
	if not data.get("campaign"):
		return {"message" : "Error. Campaign id was not provided."}
	thelist = get_ad_by_campaign(data.get('campaign'))
	ads_by_influencer = get_pending_ad_by_campaign(data.get('campaign'))
	influencers = get_influencers()
	interested = get_interest_by_campaign(data.get('campaign'))
	accepted_ads = get_accepted_ad_by_campaign(data.get('campaign'))
	rejected_ads = get_rejected_ad_by_campaign(data.get('campaign'))
	return {"ads" : thelist, "influencers" : influencers, "ads_by_influencers" : ads_by_influencer,
		 "interested" : interested, "accepted_ads" : accepted_ads, "rejected_ads" : rejected_ads}

@sponsor_backend.post('/backend/sponsor/search_influencer')
@auth_required("token")
@roles_required("sponsor")
def search():
	data = request.get_json()
	if not data.get('search_criteria'):
		return {"message" : "Error. Search criteria was not provided."}
	if not data.get('niche') and not data.get('name') and not data.get('category') and not data.get('followers'):
		return get_influencers()
	if data.get('niche'):
		thelist = search_influencer_niche(data.get('niche'))
	if data.get('name'):
		thelist = search_influencer_name(data.get('name'))
	if data.get('followers'):
		thelist = search_influencer_followers(data.get('followers'))
	if data.get('category'):
		thelist = search_influencer_category(data.get('category'))
	return thelist

@sponsor_backend.post('/backend/accept_ad')
@auth_required("token")
@roles_accepted("sponsor", "influencer")
def accept():
	data = request.get_json()
	if not data.get('ad_id'):
		return {"message" : "Error. Ad request id was not provided."}
	if not data.get('sponsor_id'):
		return {"message" : "Error. Sponsor id was not provided."}
	if not data.get('influencer_id'):
		return {"message" : "Error. Influencer id was not provided."}
	ad_request = db.session.execute(db.select(Ad_request).filter_by(id = data.get('ad_id'))).scalar()
	if not ad_request:
		return {"message" : "Error. Invalid ad request."}
	if int(ad_request.influencer_id) != int(data.get('influencer_id')):
		return {"message" : "Error. Only the influencer to whom the ad request was made can accept or reject the ad request."}
	sponsor = db.session.execute(db.select(Campaign.sponsor).filter_by(id = ad_request.campaign_id)).scalar()
	if not sponsor:
		return {"message" : "Error. Invalid sponsor."}
	if int(sponsor) != int(data.get('sponsor_id')):
		return {"message" : "Error. Only the sponsor who made the ad request can accept or reject the ad request."}
	ad_request.status = 'accepted'
	db.session.commit()
	return {"success" : "Ad request was accepted succesfully."}

@sponsor_backend.post('/backend/reject_ad')
@auth_required("token")
@roles_accepted("sponsor", "influencer")
def reject():
	data = request.get_json()
	if not data.get('ad_id'):
		return {"message" : "Error. Ad request id was not provided."}
	if not data.get('sponsor_id'):
		return {"message" : "Error. Sponsor id was not provided."}
	if not data.get('influencer_id'):
		return {"message" : "Error. Influencer id was not provided."}
	ad_request = db.session.execute(db.select(Ad_request).filter_by(id = data.get('ad_id'))).scalar()
	if not ad_request:
		return {"message" : "Error. Invalid ad request."}
	if int(ad_request.influencer_id) != int(data.get('influencer_id')):
		return {"message" : "Error. Only the influencer to whom the ad request was made can accept or reject the ad request."}
	sponsor = db.session.execute(db.select(Campaign.sponsor).filter_by(id = ad_request.campaign_id)).scalar()
	if not sponsor:
		return {"message" : "Error. Invalid sponsor."}
	if int(sponsor) != int(data.get('sponsor_id')):
		return {"message" : "Error. Only the sponsor who made the ad request can accept or reject the ad request."}
	ad_request.status = 'rejected'
	db.session.commit()
	return {"success" : "Ad request was rejected succesfully."}

@sponsor_backend.get('/download-csv')
def download_csv():
	task = create_resource.delay()
	return jsonify({"task-id" : task.id})

@sponsor_backend.get('/get-csv/<task_id>')
def get_csv(task_id):
	res = AsyncResult(task_id)
	print("I'm here 1.")
	if res.ready:
		print("I'm here 2.")
		print(res.result)
		#filename = result.result()
		return "HEhehehe"
		#return send_file(filename, as_attachment= True)
	else:
		return {"message" : "Your csv is being generated. Kindly wait a bit longer."}