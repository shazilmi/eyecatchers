from flask import request, Blueprint, jsonify
from flask_security import auth_required, roles_required
from application.sec import datastore
from database.functions import get_stats
from database.tables import Sponsor, Flagged, Influencer
from database.common import db

admin_api = Blueprint("adminapi", __name__)

@admin_api.post("/api/admin/approve_sponsor")
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
	
@admin_api.post("/api/admin/remove_flag")
@auth_required("token")
@roles_required("admin")
def remove():
	data = request.get_json()
	if not data.get('id'):
		return {"message" : "Error. Required details were not provided."}
	flagged = db.session.execute(db.select(Flagged).filter_by(id = data.get('id'))).scalar()
	if not flagged:
		return {"message" : "Error. No such flag exists."}
	db.session.delete(flagged)
	db.session.commit()
	return {"success" : "The flag was successfully removed."}

@admin_api.post('/api/admin/remove_user')
@auth_required("token")
@roles_required("admin")
def removeuser():
	data = request.get_json()
	if not data.get('id'):
		return {"message" : "Error. Required details were not provided."}
	tobedeleted = datastore.find_user(id = data.get('id'))
	if not tobedeleted:
		return {"message" : "Error. No such user exists."}
	therole = tobedeleted.roles[0].name
	if therole == 'admin':
		return {"message" : "Error. Cannot remove admin."}
	elif therole == 'sponsor':
		userdelete = db.session.execute(db.select(Sponsor).filter_by(id = data.get('id'))).scalar()
	elif therole == 'influencer':
		userdelete = db.session.execute(db.select(Influencer).filter_by(id = data.get('id'))).scalar()
	theflag = db.session.execute(db.select(Flagged).filter_by(id = data.get('id'))).scalar()
	if theflag:
		db.session.delete(theflag)
	db.session.delete(userdelete)
	datastore.delete_user(tobedeleted)
	db.session.commit()
	return {"success" : "User has been successfully removed."}
	
	
@admin_api.post("/api/admin/stats")
@auth_required("token")
@roles_required("admin")
def stats():
	thelist = get_stats()
	return thelist