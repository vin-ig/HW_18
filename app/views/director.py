from flask_restx import Namespace, Resource

from app.container import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_s = DirectorSchema()
directors_s = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
	def get(self):
		"""Выводит всех режиссеров"""
		directors = director_service.get_all()
		return directors_s.dump(directors), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
	def get(self, uid):
		"""Выводит одого режиссера"""
		director = director_service.get_one(uid)
		if director:
			return director_s.dump(director), 200
		else:
			return 'Нет режиссера с таким ID', 404
