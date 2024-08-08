from flask import Blueprint
from flask_security import auth_required, roles_required

admindashs = Blueprint('admindash', __name__)
@admindashs.route('/admindash', methods = ['GET'])
@auth_required('token')
@roles_required('admin')
def dash():
	return "Welcome admin"