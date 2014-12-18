from ..utils import *


##
# Minions

# Zombie Chow
class FP1_001:
	def deathrattle(self):
		self.heal(self.controller.opponent.hero, 5)


# Haunted Creeper
class FP1_002:
	def deathrattle(self):
		self.controller.summon("FP1_002t")
		self.controller.summon("FP1_002t")


# Mad Scientist
class FP1_004:
	def deathrattle(self):
		secrets = self.controller.deck.filterByTag(GameTag.SECRET)
		if secrets:
			self.controller.summon(random.choice(secrets))


# Nerubian Egg
class FP1_007:
	deathrattle = summonMinion("FP1_007t")


# Deathlord
class FP1_009:
	def deathrattle(self):
		minions = self.controller.opponent.deck.filterByType(CardType.MINION)
		if minions:
			self.controller.opponent.summon(random.choice(minions))


# Webspinner
class FP1_011:
	def deathrattle(self):
		self.controller.give(random.choice(self.data.entourage))


# Sludge Belcher
class FP1_012:
	deathrattle = summonMinion("FP1_012t")


# Wailing Soul
class FP1_016:
	def action(self):
		for target in self.controller.field:
			target.silence()


# Voidcaller
class FP1_022:
	def deathrattle(self):
		demons = self.controller.hand.filterByRace(Race.DEMON)
		if demons:
			self.controller.summon(random.choice(demons))


# Dark Cultist
class FP1_023:
	def deathrattle(self):
		if self.controller.field:
			random.choice(self.controller.field).buff("FP1_023e")

class FP1_023e:
	Health = 3


# Unstable Ghoul
class FP1_024:
	def deathrattle(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			self.hit(target, 1)


# Anub'ar Ambusher
class FP1_026:
	def deathrattle(self):
		if self.controller.field:
			random.choice(self.controller.field).bounce()


# Stoneskin Gargoyle
class FP1_027:
	def OWN_TURN_BEGIN(self):
		self.heal(self, self.damage)


# Undertaker
class FP1_028:
	def OWN_MINION_SUMMONED(self, minion):
		if minion.hasDeathrattle:
			self.buff("FP1_028e")

class FP1_028e:
	Atk = 1
	Health = 1


# Dancing Swords
class FP1_029:
	def deathrattle(self):
		self.controller.opponent.draw()


##
# Spells

# Reincarnate
class FP1_025:
	def action(self, target):
		target.destroy()
		self.controller.summon(target.id)


##
# Weapons

# Death's Bite
class FP1_021:
	def deathrattle(self):
		for target in self.controller.game.board:
			self.hit(target, 1)
