from flask import Blueprint
from flask_security import roles_required, auth_token_required

admindashs = Blueprint('admindash', __name__)
@admindashs.route('/admindash', methods = ['GET'])
@auth_token_required
@roles_required('admin')
def dash():
	return "Just checking to see if you're verified. You are."