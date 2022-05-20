director_ns = api.namespace('directors')


# Представления для режиссеров
@director_ns.route('/')
class DirectorsView(Resource):
	"""Вывод всех режиссеров, добавление нового"""
	def get(self):
		directors = Director.query.all()
		return directors_s.dump(directors), 200

	def post(self):
		data = request.json
		if not check_keys(data, director_keys):
			return 'Переданы неверные ключи', 200

		db.session.add(Director(**data))
		db.session.commit()
		return 'Режиссер добавлен!', 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
	"""Вывод, изменение, удаление режиссера"""
	def get(self, uid):
		director = Director.query.get(uid)
		if not director:
			return 'Нет режиссера с таким ID', 404
		return director_s.dump(director)

	def put(self, uid):
		director = Director.query.get(uid)
		if not director:
			return 'Нет режиссера с таким ID', 404

		data = request.json
		if not check_keys(data, director_keys):
			return 'Переданы неверные ключи', 200

		director.name = data.get('name')

		db.session.add(director)
		db.session.commit()
		return 'Данные режиссера обновлены', 200

	def delete(self, uid):
		director = Director.query.get(uid)
		if not director:
			return 'Нет режиссера с таким ID', 404
		db.session.delete(director)
		db.session.commit()
		return 'Режиссер удален', 200
