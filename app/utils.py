def check_keys(data: dict, allowed_keys: set) -> bool:
	"""Проверяет правильность ключей"""
	for key in data:
		if key not in allowed_keys:
			return False
	else:
		return True
