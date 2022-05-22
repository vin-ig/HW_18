from app.dao.model.genre import Genre


class GenreDAO:
	def __init__(self, session):
		self.session = session

	def get_one(self, uid):
		return self.session.query(Genre).get(uid)

	def get_all(self):
		return self.session.query(Genre).all()
