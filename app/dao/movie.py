from app.dao.model.movie import Movie

from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.constants import QUERY


class MovieDAO:
	def __init__(self, session):
		self.session = session

	def get_one(self, uid):
		return self.session.query(Movie).get(uid)

	def get_all(self):
		# select = self.session.query(*QUERY).join(Director).join(Genre)
		# if director_id and genre_id:
		# 	select = (
		# 		select
		# 			.filter(and_(Movie.director_id == director_id, Movie.genre_id == genre_id))
		# 	)
		# elif director_id:
		# 	select = select.filter(Movie.director_id == director_id)
		# elif genre_id:
		# 	select = select.filter(Movie.genre_id == genre_id)
		#
		# movies = select.all()

		return self.session.query(Movie).all()

	def create(self, data):
		movie = Movie(**data)
		self.session.add(movie)
		self.session.commit()
		return movie

	def update(self, movie):
		self.session.add(movie)
		self.session.commit()
		return movie

	def delete(self, uid):
		movie = self.get_one(uid)
		self.session.delete(movie)
		self.session.commit()
