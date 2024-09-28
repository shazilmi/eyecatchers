from flask import Blueprint

tests = Blueprint('test', __name__)
@tests.get('/test')
def test():
	return "You've been scammed."