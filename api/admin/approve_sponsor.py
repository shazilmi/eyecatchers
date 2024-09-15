from flask import request, Blueprint
from flask_security import auth_required, roles_required, current_user
from database.functions import get_sponsor_id
from database.tables import Sponsor
from database.common import db

approve_sponsor = Blueprint("api/admin/approve_sponsor", __name__)
@approve_sponsor.post("/api/admin/approve_sponsor")
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
		return {"message" : "Sponsor has been approved."}