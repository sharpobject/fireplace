def _TAG(tag, default):
	func = property(lambda self: self.tags.get(tag, default))
	@func.setter
	def _ret(self, value):
		self.setTag(tag, value)
	return _ret


def _PROPERTY(tag, default):
	func = property(lambda self: self.tags.get(tag, default) or
	                any(slot.getBoolProperty(tag) for slot in self.slots))
	@func.setter
	def _ret(self, value):
		self.setTag(tag, value)
	return _ret


class CardList(list):
	def __contains__(self, x):
		for item in self:
			if x is item:
				return True
		return False

	def contains(self, x):
		"True if list contains any instance of x"
		for item in self:
			if x == item:
				return True
		return False

	def index(self, x):
		for i, item in enumerate(self):
			if x is item:
				return i
		raise ValueError

	def remove(self, x):
		for i, item in enumerate(self):
			if x is item:
				del self[i]
				return
		raise ValueError

	def filterByTag(self, tag):
		return [card for card in self if card.tags.get(tag)]

	def filterByType(self, type):
		return [card for card in self if card.type == type]

	def filterByRace(self, race):
		return [card for card in self if card.race == race]
