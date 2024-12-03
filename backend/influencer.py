from flask import Blueprint, jsonify, request
from flask_security import auth_required, roles_required
from database.tables import Interest, Ad_request
from database.common import db
from database.functions import search_campaign_budget, search_campaign_description, search_campaign_name, search_campaign_niche, get_public_campaigns, get_ad_by_influencer, get_ad_made_by_influencer, get_ad_accepted_by_influencer, get_ad_rejected_by_influencer

influencer_backend = Blueprint("influencerbackend", __name__)

@influencer_backend.post('/backend/influencer/search_campaign')
@auth_required("token")
@roles_required("influencer")
def search():
	data = request.get_json()
	if not data.get('search_criteria'):
		return {"message" : "Error. Search criteria was not provided."}
	if not data.get('name') and not data.get('niche') and not data.get('description') and not data.get('budget'):
		return get_public_campaigns()
	if data.get('name'):
		return search_campaign_name(data.get('name'))
	if data.get('niche'):
		return search_campaign_niche(data.get('niche'))
	if data.get('budget'):
		return search_campaign_budget(data.get('budget'))
	if data.get('description'):
		return search_campaign_description(data.get('description'))
	
@influencer_backend.post('/backend/influencer/get_pending_ads')
@auth_required("token")
@roles_required("influencer")
def get_ads():
	data = request.get_json()
	if not data.get('influencer_id'):
		return {"message" : "Error. Influencer id was not provided."}
	thelist = get_ad_by_influencer(data.get('influencer_id'))
	anolist = get_ad_made_by_influencer(data.get('influencer_id'))
	accepted_ads = get_ad_accepted_by_influencer(data.get('influencer_id'))
	rejected_ads = get_ad_rejected_by_influencer(data.get('influencer_id'))
	return {"ads_for_you" : thelist, "ads_by_you" : anolist,
		 "accepted_ads" : accepted_ads, "rejected_ads" : rejected_ads}

@influencer_backend.post('/backend/influencer/express_interest')
@auth_required("token")
@roles_required("influencer")
def express():
	data = request.get_json()
	if not data.get('influencer_id'):
		return {"message" : "Error. Influencer id was not provided."}
	if not data.get('campaign_id'):
		return {"message" : "Error. Campaign id was not provided."}
	result = db.session.execute(db.select(Interest).filter((Interest.campaign_id == data.get('campaign_id')) & (Interest.influencer_id == data.get('influencer_id')))).scalar()
	if not result:
		interest = Interest(campaign_id = data.get('campaign_id'),
					 influencer_id = data.get('influencer_id'))
		db.session.add(interest)
		db.session.commit()
		return {"success" :"You have registered interest in the campaign successfully."}
	else:
		return {"message" : "Error. You have already registered interest in the campaign."}
	
@influencer_backend.post('/backend/influencer/modify_ad')
@auth_required("token")
@roles_required("influencer")
def modify():
	data = request.get_json()
	if not data.get('ad_id'):
		return {"message" : "Error. Ad request id was not provided."}
	if not data.get('requirements') or not data.get('payment_amount'):
		return {"message" : "Error. Required details were not provided."}
	ad_request = db.session.execute(db.select(Ad_request).filter_by(id = data.get('ad_id'))).scalar()
	if not ad_request:
		return {"message" : "Error. Invalid ad request."}
	ad_request.requirements = data.get('requirements')
	ad_request.payment_amount = data.get('payment_amount')
	ad_request.made_by = 'influencer'
	db.session.commit()
	return {"success" : "Ad request has been negotiated successfully"}