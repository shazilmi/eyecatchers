from flask import Blueprint, request, render_template
from flask_security import roles_required, current_user
from database.tables import Campaign
from database.common import db
from datetime import date

create_campaigns = Blueprint('create_campaign', __name__)
@create_campaigns.route('/create_campaign', methods = ['GET', 'POST'])
@roles_required('sponsor')
def create_campaign():
	if request.method == 'GET':
		return render_template('sponsor/create_campaign.html')
	if request.method == 'POST':
		campaign_name = request.form['name']
		campaign_description = request.form['description']
		sponsor_id = current_user.id
		start = request.form['start_date']
		start_date = [int(start[0:4]), int(start[5:7]), int(start[8:10])]
		end = request.form['end_date']
		end_date = [int(end[0:4]), int(end[5:7]), int(end[8:10])]
		campaign_budget = request.form['budget']
		campaign_niche = request.form['niche']
		campaign_visibility = request.form['visibility']
		campaign_goals = request.form['goals']
		campaign = Campaign(name = campaign_name, description = campaign_description, 
					  sponsor = sponsor_id,
					    start_date = date(start_date[0], start_date[1], start_date[2]), 
						end_date = date(end_date[0], end_date[1], end_date[2]), 
					  budget = campaign_budget, visibility = campaign_visibility, 
					  goals = campaign_goals, niche = campaign_niche)
		db.session.add(campaign)
		db.session.commit()
		return 'Done'