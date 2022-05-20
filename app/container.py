from app.dao.movie import MovieDAO
from app.services.movie import MovieService
from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

# director_dao = DirectorMovieDAO(db.session)
# director_service = DirectorMovieService(director_dao)
