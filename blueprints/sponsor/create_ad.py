from flask import Blueprint, request, render_template, session
from flask_security import roles_required, current_user, auth_required
from database.tables import Ad_request
from database.common import db
from database.functions import get_campaign

create_ads = Blueprint('create_ad', __name__)
@create_ads.route('/create_ad', methods = ['GET', 'POST'])
@auth_required('token')
@roles_required('sponsor')
def create_ad():
	if request.method == 'GET':
		campaigns = get_campaign(current_user.id)
		return render_template('sponsor/choose_create_ad.html', thelist = campaigns)
	if request.method == 'POST':
		try:
			session['campaign'] = request.form['theid']
			return render_template('sponsor/create_ad.html')
		except:
			req = request.form['requirements']
			amount = request.form['amount']
			ad = Ad_request(campaign_id = session['campaign'], requirements = req, 
				   payment_amount = amount, status = 'ongoing')
			db.session.add(ad)
			db.session.commit()
			return 'Done'