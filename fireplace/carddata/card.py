from ..targeting import *
from ..xmlcard import XMLCard as Card
from .helpers import *


def on(event):
	def decorator(func):
		func.event = event
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
		return wrapper
	return decorator
