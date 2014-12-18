from ..utils import *

##
# Minions

# Blood Imp
class CS2_059:
	def OWN_TURN_END(self):
		if self.controller.field:
			random.choice(self.controller.field).buff("CS2_059o")

class CS2_059o:
	Health = 1


# Felguard
class EX1_301:
	def action(self):
		self.controller.maxMana -= 1


# Succubus
class EX1_306:
	action = discard(1)


# Doomguard
class EX1_310:
	action = discard(2)


# Pit Lord
class EX1_313:
	def action(self):
		self.hit(self.controller.hero, 5)


# Flame Imp
class EX1_319:
	def action(self):
		self.hit(self.controller.hero, 3)


# Lord Jaraxxus
class EX1_323:
	def action(self):
		self.removeFromField()
		self.controller.summon("EX1_323h")
		self.controller.summon("EX1_323w")


##
# Spells

# Drain Life
class CS2_061:
	def action(self, target):
		self.hit(target, 2)
		self.heal(self.controller.hero, 2)


# Hellfire
class CS2_062:
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_CHARACTERS):
			self.hit(target, 3)


# Shadow Bolt
class CS2_057:
	action = damageTarget(4)


# Mortal Coil
class EX1_302:
	def action(self, target):
		self.hit(target, 1)
		if target.zone == Zone.GRAVEYARD:
			self.controller.draw()


# Shadowflame
class EX1_303:
	def action(self, target):
		for minion in self.controller.opponent.field:
			self.hit(minion, target.atk)
		target.destroy()


# Soulfire
class EX1_308:
	def action(self, target):
		self.hit(target, 4)
		if self.controller.hand:
			random.choice(self.controller.hand).discard()


# Siphon Soul
class EX1_309:
	def action(self, target):
		self.heal(self.controller.hero, 3)
		target.destroy()


# Twisting Nether
class EX1_312:
	def action(self):
		for minion in self.controller.getTargets(TARGET_ALL_MINIONS):
			target.destroy()


# Power Overwhelming
class EX1_316:
	action = buffTarget("EX1_316e")

class EX1_316e:
	Atk = 4
	Health = 4
	def TURN_END(self, player):
		self.owner.destroy()


# Sense Demons
class EX1_317:
	def action(self):
		for i in range(2):
			demons = self.controller.deck.filterByRace(Race.DEMON)
			if demons:
				self.controller.addToHand(random.choice(demons))
			else:
				self.controller.give("EX1_317t")


# Bane of Doom
class EX1_320:
	def action(self, target):
		self.hit(target, 2)
		if target.zone == Zone.GRAVEYARD:
			self.controller.summon(random.choice(self.data.entourage))


# Demonfire
class EX1_596:
	def action(self, target):
		if target.race == Race.DEMON and target.controller == self.controller:
			target.buff("EX1_596e")
		else:
			self.hit(target, 2)

class EX1_596e:
	Atk = 2
	Health = 2


# Sacrificial Pact
class NEW1_003:
	def action(self, target):
		target.destroy()
		self.heal(self.controller.hero, 5)
