from ..targeting import *
from ..enums import Zone
from ..xmlcard import XMLCard
from ..entity import on
from .helpers import *


class Card(XMLCard):
	def __new__(cls, id):
		instance = super().__new__(cls)
		cls._eventListeners = {}
		for name, func in cls.__dict__.items():
			if name == "inPlay":
				# TODO multiple defs for same zone
				cls._eventListeners[Zone.PLAY] = {func.event: func}
		return instance
