from ..targeting import *
from ..enums import Zone
from ..xmlcard import XMLCard
from .helpers import *


def on(event):
	def decorator(func):
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		wrapper.event = event
		return wrapper
	return decorator


class Card(XMLCard):
	def __new__(cls, id):
		instance = super().__new__(cls)
		cls._eventListeners = {}
		for name, func in cls.__dict__.items():
			if name == "inPlay":
				# TODO multiple defs for same zone
				cls._eventListeners[Zone.PLAY] = {func.event: func}
		return instance
