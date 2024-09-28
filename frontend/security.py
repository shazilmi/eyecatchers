from flask import Blueprint, render_template
from flask_security import anonymous_user_required, login_required, anonymous_user_required

security_bp = Blueprint('flasksecurity', __name__)

@security_bp.get('/signup')
@anonymous_user_required
def signup():
	return render_template('security/signup.html', logged_in = False)

@security_bp.get('/signin')
@anonymous_user_required
def login():
	return render_template('security/login.html', logged_in = False)

@security_bp.get('/signout')
@login_required
def logout():
	return render_template('security/logout.html', logged_in = False)