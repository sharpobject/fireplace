from ..utils import *

##
# Minions

# Archmage Antonidas
class EX1_559:
	def OWN_CARD_PLAYED(self, card):
		if card.type == CardType.SPELL:
			self.controller.give("CS2_029")


# Mana Wyrm
class NEW1_012:
	def OWN_CARD_PLAYED(self, card):
		if card.type == CardType.SPELL:
			self.buff("NEW1_012o")

class NEW1_012o:
	Atk = 1


##
# Spells

# Arcane Intellect
class CS2_023:
	action = drawCards(2)


# Frostbolt
class CS2_024:
	def action(self, target):
		self.hit(target, 3)
		target.frozen = True


# Arcane Explosion
class CS2_025:
	def action(self):
		for target in self.controller.getTargets(TARGET_ENEMY_MINIONS):
			self.hit(target, 1)


# Frost Nova
class CS2_026:
	def action(self):
		for target in self.controller.getTargets(TARGET_ENEMY_MINIONS):
			target.frozen = True


# Mirror Image
class CS2_027:
	def action(self):
		self.controller.summon("CS2_mirror")
		self.controller.summon("CS2_mirror")


# Blizzard
class CS2_028:
	def action(self):
		for target in self.controller.getTargets(TARGET_ENEMY_MINIONS):
			self.hit(target, 2)
			target.frozen = True


# Fireball
class CS2_029:
	action = damageTarget(6)


# Ice Lance
class CS2_031:
	def action(self, target):
		if target.frozen:
			self.hit(target, 4)
		else:
			target.frozen = True


# Cone of Cold
class EX1_275:
	def action(self, target):
		for minion in target.adjacentMinions:
			self.hit(minion, 1)
			minion.frozen = True
		self.hit(target, 1)
		target.frozen = True


# Pyroblast
class EX1_279:
	action = damageTarget(10)
