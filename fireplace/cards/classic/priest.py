import random
from fireplace.enums import CardType


##
# Minions


# Northshire Cleric
class CS2_235:
	def HEAL(self, source, target, amount):
		if target.type == CardType.MINION:
			self.controller.draw()


# Lightwarden
class EX1_001:
	def HEAL(self, source, target, amount):
		self.buff("EX1_001e")

class EX1_001e:
	Atk = 2


# Cabal Shadow Priest
class EX1_091:
	def action(self, target):
		self.controller.takeControl(target)


# Lightspawn
class EX1_335:
	def UPDATE(self):
		if self.atk != self.health:
			# self.atk = self.health
			# Haha! You thought this would be that easy, huh? THINK AGAIN!
			# Attack is the sum of the ATK of the entity and all its slots.
			# This matters because auras are applied to lightspawn, and lightspawn
			# doesn't actually respect those auras.
			# Now, we can either hack around this with internal buffs, tags etc... or we
			# can set the attack to *less* than the health, taking buffs into account.
			# Incidentally, this means that Lightspawn's GameTag.ATK can go negative.
			# Tell me, Blizzard, is it really such a coincidence its base attack is 0?
			self.atk = self.health - self.extraAtk


# Lightwell
class EX1_341:
	def OWN_TURN_BEGIN(self):
		targets = [t for t in self.controller.getTargets(TARGET_FRIENDLY_CHARACTERS) if t.damage]
		self.heal(random.choice(targets), 3)


# Temple Enforcer
class EX1_623:
	action = buffTarget("EX1_623e")

class EX1_623e:
	Health = 3


# Dark Cultist
class FP1_023:
	def deathrattle(self):
		if self.controller.field:
			random.choice(self.controller.field).buff("FP1_023e")

class FP1_023e:
	Health = 3


##
# Spells

# Power Word: Shield
class CS2_004(Card):
	def action(self, target):
		target.buff("CS2_004e")
		self.controller.draw()

class CS2_004e(Card):
	Health = 2


# Holy Nova
class CS1_112(Card):
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_CHARACTERS):
			if target.controller == self.controller:
				self.heal(target, 2)
			else:
				self.hit(target, 2)


# Mind Control
class CS1_113(Card):
	def action(self, target):
		self.controller.takeControl(target)


# Mind Vision
class CS2_003(Card):
	def action(self):
		if self.controller.opponent.hand:
			self.controller.give(random.choice(self.controller.opponent.hand).id)


# Shadow Word: Pain
class CS2_234(Card):
	action = destroyTarget


# Mind Blast
class DS1_233(Card):
	action = damageEnemyHero(5)


# Silence
class EX1_332(Card):
	action = silenceTarget


# Thoughtsteal
class EX1_339(Card):
	def action(self):
		deck = self.controller.opponent.deck
		for card in random.sample(deck, min(len(deck), 2)):
			self.controller.give(card.id)


# Mindgames
class EX1_345(Card):
	def action(self):
		creatures = [c for c in self.controller.opponent.deck if c.type == CardType.MINION]
		if creatures:
			creature = random.choice(creatures).id
		else:
			creature = "EX1_345t"
		self.controller.summon(creature)


# Circle of Healing
class EX1_621(Card):
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			self.heal(target, 4)


# Shadow Word: Death
class EX1_622(Card):
	action = destroyTarget


# Holy Fire
class EX1_624(Card):
	def action(self, target):
		self.hit(target, 5)
		self.heal(self.controller.hero, 5)
