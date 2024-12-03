from flask import request, Blueprint, jsonify
from flask_security import auth_required, roles_required
from application.sec import datastore
from database.functions import get_stats, get_pending_approvals
from database.tables import Sponsor, Influencer
from database.common import db

admin_backend = Blueprint("adminbackend", __name__)

@admin_backend.get("/backend/admin/approve_sponsor")
@auth_required("token")
@roles_required("admin")
def get_pending():
	thelist = get_pending_approvals()
	return thelist

@admin_backend.post("/backend/admin/approve_sponsor")
@auth_required("token")
@roles_required("admin")
def approve():
	data = request.get_json()
	if not data.get('id'):
		return {"message" : "Error. ID of sponsor to be approved was not provided."}
	sponsor = db.session.execute(db.select(Sponsor).filter_by(id = data.get('id'))).scalar()
	if not sponsor:
		return {"message" : "Error. No such sponsor exists."}
	if sponsor.approved == True:
		return {"message" : "The selected sponsor is already approved."}
	else:
		sponsor.approved = True
		db.session.commit()
		return {"success" : "Sponsor has been approved."}
	
	
@admin_backend.post("/backend/admin/stats")
@auth_required("token")
@roles_required("admin")
def stats():
	thelist = get_stats()
	return thelist