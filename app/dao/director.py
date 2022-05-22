from app.dao.model.director import Director


class DirectorDAO:
	def __init__(self, session):
		self.session = session

	def get_one(self, uid):
		return self.session.query(Director).get(uid)

	def get_all(self):
		return self.session.query(Director).all()
