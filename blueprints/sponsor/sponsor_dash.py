from flask import Blueprint
from flask_security import roles_required, auth_required

sponsordashs = Blueprint('sponsordash', __name__)
@sponsordashs.route('/sponsordash', methods = ['GET'])
@auth_required('token')
@roles_required('sponsor')
def dash():
	return "Just checking to see if you're verified. You are."