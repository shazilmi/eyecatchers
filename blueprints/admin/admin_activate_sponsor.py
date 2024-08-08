from flask import Blueprint
from flask_security import auth_required, roles_required
from database.tables import User
from database.common import db

adminapprovals = Blueprint('adminapproval', __name__)
@adminapprovals.route('/adminapproval/<int:id>', methods = ['GET'])
@auth_required("token")
@roles_required("admin")
def approve(id):
	sponsor = User.query.get(id)
	if not sponsor or "sponsor" not in sponsor.roles:
		return "No user exists."
	sponsor.active = True
	db.session.commit()
	return "Success"