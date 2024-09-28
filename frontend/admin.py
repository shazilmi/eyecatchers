from flask import Blueprint, render_template
from flask_security import login_required, roles_required
from database.functions import get_pending_approvals, get_flagged

admin_frontend = Blueprint('admin_frontend', __name__)

@admin_frontend.get('/admin/dash')
@login_required
@roles_required('admin')
def dashboard():
	return render_template('admin/dash.html')

@admin_frontend.get('/admin/stats')
@login_required
@roles_required('admin')
def dash():
	return render_template('admin/stats.html')

@admin_frontend.get('/admin/approve_sponsor')
@login_required
@roles_required('admin')
def approve():
	thelist = get_pending_approvals()
	return render_template('admin/approve_sponsor.html', thelist = thelist,listlength = len(thelist))

@admin_frontend.get('/admin/remove_flagged')
@login_required
@roles_required('admin')
def remove():
	thelist = get_flagged()
	return render_template('admin/remove_flagged.html', thelist = thelist, listlength = len(thelist))