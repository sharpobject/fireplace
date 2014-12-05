from .enums import Zone

def on(event):
	def decorator(func):
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		wrapper.event = event
		return wrapper
	return decorator


class Entity(object):
	def __init__(self):
		self.tags = {}

	def __new__(cls, *args, **kwargs):
		instance = super().__new__(cls)
		cls._eventListeners = {}
		for name, func in cls.__dict__.items():
			if name.isupper() and hasattr(func, "__call__"):
				# TODO multiple defs for same zone
				cls._eventListeners[name] = [func]
		return instance

	def broadcast(self, event, *args):
		for entity in self.entities:
			for k, funcs in self._eventListeners.items():
				if event == k:
					for f in funcs:
						f(self, *args)
		if event != "UPDATE":
			self.broadcast("UPDATE")

	def setTag(self, tag, value):
		self.tags[tag] = value

	def unsetTag(self, tag):
		del self.tags[tag]

	def getIntProperty(self, tag):
		ret = self.tags.get(tag, 0)
		for slot in self.slots:
			ret += slot.getIntProperty(tag)
		return ret

	def getBoolProperty(self, tag):
		if self.tags.get(tag, False):
			return True
		for slot in self.slots:
			if slot.getBoolProperty(tag):
				return True
		return
