from flask import Blueprint, request
from flask_security import auth_required, roles_required
from database.tables import User, Role
from database.common import db

userlogins = Blueprint('login', __name__)
@userlogins.route('/login', methods = ['GET', 'POST'])
if request.method == 'GET':
	return "Login html page"
elif request.method == "POST":
	return "Something"