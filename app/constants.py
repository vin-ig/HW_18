from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie

# Запрос для формирования корректного вывода фильмов

QUERY = (
	Movie.id,
	Movie.title,
	Movie.description,
	Movie.trailer,
	Movie.year,
	Movie.rating,
	Director.name.label('director'),
	Genre.name.label('genre')
)

# Допустимые ключи для проверки
movie_keys = {'title', 'description', 'trailer', 'year', 'rating', 'genre_id', 'director_id'}
director_keys = {'name'}
genre_keys = {'name'}
