from flask import Blueprint, request, render_template
from flask_security import roles_required, current_user
from database.tables import Ad_request
from database.common import db
from database.functions import get_ad

delete_ads = Blueprint('delete_ad', __name__)
@delete_ads.route('/delete_ad', methods = ['GET', 'POST'])
@roles_required('sponsor')
def delete_ad():
	if request.method == 'GET':
		ads = get_ad(current_user.id)
		print(ads)
		print(ads[0][0])
		return render_template('sponsor/delete_ad.html', thelist = ads)
	if request.method == 'POST':
		ad_id = request.form['theid']
		thead = db.session.execute(db.select(Ad_request).filter_by(id = ad_id)).scalar_one()
		db.session.delete(thead)
		db.session.commit()
		return 'Done'