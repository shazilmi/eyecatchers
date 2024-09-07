from flask import Blueprint, render_template, request
from flask_security import roles_required, current_user
from database.tables import Campaign
from database.common import db
from database.functions import get_campaign

delete_campaigns = Blueprint('delete_campaign', __name__)
@delete_campaigns.route('/delete_campaign', methods = ['GET', 'POST'])
@roles_required('sponsor')
def delete_campaign():
	if request.method == 'GET':
		campaigns = get_campaign(current_user.id)
		return render_template('sponsor/delete_campaign.html', thelist = campaigns)
	if request.method == 'POST':
		campaign_id = request.form['theid']
		thecampaign = db.session.execute(db.select(Campaign).filter_by(id = campaign_id)).scalar_one()
		db.session.delete(thecampaign)
		db.session.commit()
		return 'Done'