from flask import Blueprint
from flask_security import roles_required

admindashs = Blueprint('admindash', __name__)
@admindashs.route('/admindash', methods = ['GET'])
@roles_required('admin')
def dash():
	return "Welcome admin"