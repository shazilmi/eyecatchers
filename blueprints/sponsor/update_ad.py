from flask import Blueprint, request, render_template, session
from flask_security import roles_required, current_user
from database.tables import Ad_request
from database.common import db
from database.functions import get_ad, get_ad_details

update_ads = Blueprint('update_ad', __name__)
@update_ads.route('/update_ad', methods = ['GET', 'POST'])
@roles_required('sponsor')
def update_ad():
	if request.method == 'GET':
		ads = get_ad(current_user.id)
		return render_template('sponsor/choose_update_ad.html', thelist = ads)
	if request.method == 'POST':
		try:
			ad_id = request.form['theid']
			session['ad'] = ad_id
			details = get_ad_details(ad_id)
			return render_template('sponsor/update_ad.html', thelist = details)
		except:
			thead = db.session.execute(db.select(Ad_request).filter_by(id = session['ad'])).scalar_one()
			thead.requirements = request.form['requirements']
			thead.status = request.form['status']
			thead.payment_amount = request.form['payment_amount']
			db.session.commit()
			session.pop('ad', None)
			return 'Done'