from flask_restx import Namespace, Resource
from flask import request
from sqlalchemy import or_, and_, exc

from app.constants import movie_keys
from app.container import movie_service
from app.dao.model.movie import Movie, MovieSchema
from app.utils import check_keys

movie_ns = Namespace('movies')

# Создаем экземпляры классов схем сериализации
movie_s = MovieSchema()
movies_s = MovieSchema(many=True)


# Представления для фильмов
@movie_ns.route('/')
class MoviesView(Resource):
	"""Вывод нескольких фильмов, добавление нового в БД"""
	def get(self):
		director_id = request.values.get('director_id')
		genre_id = request.values.get('genre_id')

		# Разделяем вывод фильмов на страницы
		# try:
		# 	page = int(request.values.get('page'))
		# 	lim = int(request.values.get('limit'))
		# except (TypeError, ValueError):
		# 	page = 1
		# 	lim = Movie.query.count()
		# offs = (page - 1) * lim
		#
		# param = Movie.director_id == director_id, Movie.genre_id == genre_id
		# if director_id and genre_id:
		# 	movies = db.session.query(*query_).join(Director).join(Genre).filter(and_(*param)).all()
		# elif director_id or genre_id:
		# 	movies = db.session.query(*query_).join(Director).join(Genre).filter(or_(*param)).all()
		# else:
		# 	movies = db.session.query(*query_).join(Director).join(Genre).limit(lim).offset(offs).all()

		movies = movie_service.get_all()
		return movies_s.dump(movies), 200

	def post(self):
		data = request.json
		if not check_keys(data, movie_keys):
			return 'Переданы неверные ключи', 200
		movie_service.create(data)
		return 'Фильм добавлен!', 200


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
	"""Вывод, изменение, удаление одного фильма"""
	def get(self, uid):
		try:
			# movie = db.session.query(QUERY).join(Director).join(Genre).filter(Movie.id == uid).one()
			movie = movie_service.get_one(uid)
			return movie_s.dump(movie), 200
		except exc.NoResultFound:
			return 'Нет фильма с таким ID', 404

	def put(self, uid):
		if not movie_service.get_one(uid):
			return 'Нет фильма с таким ID', 404

		data = request.json
		if not check_keys(data, movie_keys):
			return 'Переданы неверные ключи', 200

		movie_service.update(data, uid)
		return 'Данные фильма обновлены', 200

	def patch(self, uid):
		if not movie_service.get_one(uid):
			return 'Нет фильма с таким ID', 404

		data = request.json
		if not check_keys(data, movie_keys):
			return 'Переданы неверные ключи', 200

		movie_service.update(data, uid)
		return 'Данные фильма обновлены', 200

	def delete(self, uid):
		if not movie_service.get_one(uid):
			return 'Нет фильма с таким ID', 404
		movie_service.delete(uid)
		return 'Фильм удален', 200
