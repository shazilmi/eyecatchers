from flask import request, Blueprint, jsonify
from flask_security import auth_required, roles_accepted
from database.tables import Flagged, Sponsor, Influencer, User
from database.common import db

common_api = Blueprint('commonapi', __name__)

@common_api.post('/api/flag_user')
@auth_required("token")
@roles_accepted('admin', 'influencer', 'sponsor')
def flag():
	data = request.get_json()
	if not data.get('id') or not data.get('flagged_by') or not data.get('reason') or not data.get('role'):
		return {"message" : "Error. Required details were not provided.", "request" : data}
	if data.get('role') == 'sponsor':
		to_flag = db.session.execute(db.select(Sponsor).filter_by(id = data.get('id'))).scalar()
	elif data.get('role') == 'influencer':
		to_flag = db.session.execute(db.select(Influencer).filter_by(id = data.get('id'))).scalar()
	else:
		return {"message" : "Error. Admin cannot be flagged."}
	if not to_flag:
		return {"message" : "Error. No such user was found."}
	check_user = db.session.execute(db.select(User).filter_by(id = data.get('flagged_by'))).scalar()
	if not check_user:
		return {"message" : "Error. Flagged by non-existent user."}
	check_flag = db.session.execute(db.select(Flagged).filter_by(id = data.get('id'))).scalar()
	if not check_flag:
		new_flag = Flagged(id = data.get('id'), reason = data.get('reason'), flagged_by = data.get('flagged_by'))
		db.session.add(new_flag)
		db.session.commit()
		return {"success" : "User has been flagged."}
	else:
		return {"success" : "User has already been flagged."}