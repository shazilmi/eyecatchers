from flask import Blueprint, render_template, redirect
from flask_security import current_user, login_required

about_ec = Blueprint('about', __name__)

@about_ec.get('/about')
def about():
	if current_user.is_authenticated:
		return render_template('about.html', logged_in = True)
	else:
		return render_template('about.html', logged_in = False)
	
@about_ec.get('/dash')
@login_required
def dash():
	if current_user.roles[0].name == 'admin':
		return redirect('admin/dash')
	elif current_user.roles[0].name == 'sponsor':
		return redirect('sponsor/dash')
	else:
		return redirect('influencer/dash')