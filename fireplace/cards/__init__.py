import os
import json
from importlib import import_module


# Here we will import every card from every set.
# For every card, we will "merge" the class with its compiled definition.
# This code is only ran once, at initial import.

with open(os.path.join(os.path.dirname(__file__), "db.json"), "r") as f:
	_db = json.load(f)

for set in ("classic", ):
	module = import_module("." + set, package="fireplace.cards")
	for k, cls in module.__dict__.items():
		if not k.startswith("_"):
			if k in _db:
				for tag, value in _db[k].items():
					setattr(cls, tag, value)
				globals()[k] = cls
