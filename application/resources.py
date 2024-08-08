from flask_restful import Resource, Api, reqparse, marshal_with, fields

api = Api(prefix = '/api')

parser = reqparse.RequestParser()
parser.add_argument('topic', type = str, help = 'It did not work.')
parser.add_argument('description', type = str, help = 'It did not work.')

class something(Resource):
	def get(self):
		return {"message" : "Hahaha!"}
	
	def post(self):
		args = parser.parse_args
		

api.add_resource(something, '/something')