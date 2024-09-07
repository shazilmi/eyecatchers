from flask import Blueprint, request, render_template, session
from flask_security import roles_required, current_user
from database.tables import Campaign
from database.common import db
from datetime import date
from database.functions import get_campaign, get_campaign_details

update_campaigns = Blueprint('update_campaign', __name__)
@update_campaigns.route('/update_campaign', methods = ['GET', 'POST'])
@roles_required('sponsor')
def update_campaign():
	if request.method == 'GET':
		campaigns = get_campaign(current_user.id)
		return render_template('sponsor/choose_update_campaign.html', thelist = campaigns)
	if request.method == 'POST':
		try:
			campaign_id = request.form['theid']
			session['campaign'] = campaign_id
			details = get_campaign_details(campaign_id)
			return render_template('sponsor/update_campaign.html', thelist = details)
		except:
			thecampaign = db.session.execute(db.select(Campaign).filter_by(id = session['campaign'])).scalar_one()
			thecampaign.name = request.form['name']
			thecampaign.description = request.form['description']
			start_date = request.form['start_date']
			start = [int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])]
			thecampaign.start_date = date(start[0], start[1], start[2])
			end = request.form['end_date']
			end_date = [int(end[0:4]), int(end[5:7]), int(end[8:10])]
			thecampaign.end_date = date(end_date[0], end_date[1], end_date[2])
			thecampaign.budget = request.form['budget']
			thecampaign.niche = request.form['niche']
			thecampaign.visibility = request.form['visibility']
			thecampaign.goals = request.form['goals']
			session.pop('campaign', None)
			db.session.commit()
			return 'Done'