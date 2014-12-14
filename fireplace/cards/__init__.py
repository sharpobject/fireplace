import os
from ..enums import GameTag
from .game import *
from .classic import *
from .naxxramas import *
from . import cardxml


# Here we will import every card from every set.
# For every card, we will "merge" the class with its compiled definition.
# This code is only ran once, at initial import.

_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, "data", "TextAsset", "enUS.txt")

tagmap = {
	GameTag.ATK: "Atk",
	GameTag.CHARGE: "Charge",
	GameTag.DEATH_RATTLE: "Deathrattle",
	GameTag.DURABILITY: "Durability",
	GameTag.HEALTH: "Health",
	GameTag.CARDNAME: "Name",
	GameTag.RECALL: "Recall",
	GameTag.SECRET: "Secret",
	GameTag.TAUNT: "Taunt",
}

tagnames = {
	"Atk": GameTag.ATK,
	"Charge": GameTag.CHARGE,
	"Durability": GameTag.DURABILITY,
	"Deathrattle": GameTag.DEATH_RATTLE,
	"Health": GameTag.HEALTH,
	"Recall": GameTag.RECALL,
	"Taunt": GameTag.TAUNT,
	"cantAttack": GameTag.CANT_ATTACK, # XXX
}

def merge(xmlcard, carddef):
	if not carddef:
		cls = type(xmlcard.id, (), {})
	else:
		cls = type(xmlcard.id, (carddef, ), {})
	cls.tags = xmlcard.tags
	if carddef:
		for attr, value in carddef.__dict__.items():
			if attr in tagnames:
				cls.tags[tagnames[attr]] = value
	cls.requirements = xmlcard.requirements
	cls.entourage = xmlcard.entourage
	return cls

with open(_PATH, "r") as f:
	db = cardxml.load(_PATH)
	for id, card in db.items():
		carddef = globals().get(id)
		globals()[id] = merge(card, carddef)
