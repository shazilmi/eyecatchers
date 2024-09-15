from flask import Blueprint
from flask_security import roles_required, auth_required

influencerdashs = Blueprint('influencerdash', __name__)
@influencerdashs.route('/influencerdash', methods = ['GET'])
@auth_required('token')
@roles_required('influencer')
def dash():
	return "Just checking to see if you're verified. You are."