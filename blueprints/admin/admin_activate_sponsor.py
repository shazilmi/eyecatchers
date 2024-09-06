from flask import Blueprint, request, render_template
from flask_security import auth_required, roles_required
from database.functions import get_pending_approvals
from application.sec import datastore
from database.common import db
from database.tables import Sponsor

adminapprovals = Blueprint('adminapproval', __name__)
@adminapprovals.route('/adminapproval', methods = ['GET', 'POST'])
@roles_required("admin")
def approve():
	if request.method == 'GET':
		not_approved = get_pending_approvals()
		return render_template('admin/sponsor_approval.html', thelist = not_approved)
	if request.method == 'POST':
		theid = request.form['theid']
		sponsor = db.session.execute(db.select(Sponsor).filter_by(id = theid)).scalar_one()
		sponsor.approved = True
		db.session.commit()
		return "Approved."