from ..utils import *


# The Black Knight
class EX1_002:
	action = destroyTarget


# Bloodmage Thalnos
class EX1_012:
	deathrattle = drawCard


# King Mukla
class EX1_014:
	def action(self):
		self.controller.opponent.give("EX1_014t")
		self.controller.opponent.give("EX1_014t")

# Bananas
class EX1_014t:
	action = buffTarget("EX1_014te")

class EX1_014te:
	Atk = 1
	Health = 1


# Sylvanas Windrunner
class EX1_016:
	def deathrattle(self):
		if self.controller.opponent.field:
			self.controller.takeControl(random.choice(self.controller.opponent.field))


# Lorewalker Cho
class EX1_100:
	def CARD_PLAYED(self, player, card):
		if card.type == CardType.SPELL:
			player.opponent.give(card.id)


# Cairne Bloodhoof
class EX1_110:
	deathrattle = summonMinion("EX1_110t")


# Leeroy Jenkins
class EX1_116:
	def action(self):
		self.controller.opponent.summon("EX1_116t")
		self.controller.opponent.summon("EX1_116t")


# Baron Geddon
class EX1_249:
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			if target is not self:
				self.hit(target, 2)


# Ragnaros the Firelord
class EX1_298:
	cantAttack = True
	def OWN_TURN_END(self):
		self.hit(random.choice(self.controller.getTargets(TARGET_ENEMY_CHARACTERS)), 8)


# Nat Pagle
class EX1_557:
	def OWN_TURN_BEGIN(self):
		if random.choice((0, 1)):
			self.controller.draw()


# Harrison Jones
class EX1_558:
	def action(self):
		weapon = self.controller.opponent.hero.weapon
		if weapon:
			weapon.destroy()
			self.controller.draw(weapon.durability)


# Malygos
class EX1_563:
	spellpower = 5


# The Beast
class EX1_577:
	def deathrattle(self):
		self.controller.opponent.summon("EX1_finkle")


# Illidan Stormrage
class EX1_614:
	def OWN_CARD_PLAYED(self, card):
		self.controller.summon("EX1_614t")


# Deathwing
class NEW1_030:
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			# Let's not kill ourselves in the process
			if target is not self:
				target.destroy()
		self.controller.discardHand()


# Hogger
class NEW1_040:
	OWN_TURN_END = summonMinion("NEW1_040t")


# Elite Tauren Chieftain
class PRO_001:
	def action(self):
		self.controller.give(random.choice(self.data.entourage))
		self.controller.opponent.give(random.choice(self.data.entourage))

# I Am Murloc
class PRO_001a:
	def action(self):
		for i in range(random.choice((3, 4, 5))):
			self.controller.summon("PRO_001at")

# Rogues Do It...
class PRO_001b:
	def action(self, target):
		target.damage(4)
		self.controller.draw()


# Power of the Horde
class PRO_001c:
	def action(self):
		self.controller.summon(random.choice(self.data.entourage))
