from flask import Blueprint, request, render_template
from flask_security import roles_required
from database.functions import get_stats

adminstats = Blueprint('adminstats', __name__)
@adminstats.route('/adminstats', methods = ['GET'])
@roles_required('admin')
def stats():
	if request.method == 'GET':
		statlist = get_stats()
		return render_template('admin/admin_stats.html', stats = statlist)