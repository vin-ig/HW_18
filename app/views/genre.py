from flask_restx import Namespace, Resource

from app.container import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_s = GenreSchema()
genres_s = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
	def get(self):
		"""Выводит все жанры"""
		genres = genre_service.get_all()
		return genres_s.dump(genres), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
	def get(self, uid):
		"""Выводит один жанр"""
		genre = genre_service.get_one(uid)
		if genre:
			return genre_s.dump(genre), 200
		else:
			return 'Нет жанра с таким ID', 404
