from ..utils import *

##
# Minions

# Armorsmith
class EX1_402:
	def OWN_DAMAGE(self, source, target, amount):
		if target.type == CardType.MINION:
			self.controller.hero.armor += 1


# Cruel Taskmaster
class EX1_603:
	def action(self, target):
		target.buff("EX1_603e")
		self.hit(target, 1)

class EX1_603e:
	Atk = 2


# Frothing Berserker
class EX1_604:
	def DAMAGE(self, source, target, amount):
		if target.type == CardType.MINION:
			self.buff("EX1_604o")

class EX1_604o:
	Atk = 1


##
# Spells

# Charge
class CS2_103:
	action = buffTarget("CS2_103e2")

class CS2_103e2:
	Atk = 2
	Charge = True


# Rampage
class CS2_104:
	action = buffTarget("CS2_104e")

class CS2_104e:
	Atk = 3
	Health = 3


# Heroic Strike
class CS2_105:
	action = buffSelf("CS2_105e")

class CS2_105e:
	Atk = 4


# Execute
class CS2_108:
	action = destroyTarget


# Cleave
class CS2_114:
	def action(self):
		targets = random.sample(self.controller.opponent.field, 2)
		for target in targets:
			self.hit(target, 2)


# Slam
class EX1_391:
	def action(self, target):
		self.hit(target, 2)
		if target.zone == Zone.PLAY:
			self.controller.draw()


# Battle Rage
class EX1_392:
	def action(self):
		for target in self.controller.getTargets(TARGET_FRIENDLY_CHARACTERS):
			if target.damage:
				self.controller.draw()


# Whirlwind
class EX1_400:
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			self.hit(target, 1)


# Brawl
class EX1_407:
	def action(self):
		board = self.controller.getTargets(TARGET_ALL_MINIONS)
		for minion in random.sample(board, len(board) - 1):
			minion.destroy()


# Mortal Strike
class EX1_408:
	def action(self, target):
		self.hit(target, 6 if self.controller.hero.health <= 12 else 4)


# Upgrade!
class EX1_409:
	def action(self):
		if self.controller.hero.weapon:
			self.controller.hero.weapon.buff("EX1_409e")
			self.controller.hero.weapon.durability += 1
		else:
			self.controller.summon("EX1_409t")

class EX1_409e:
	Atk = 1


# Shield Slam
class EX1_410:
	def action(self, target):
		self.hit(target, self.controller.hero.armor)


# Shield Block
class EX1_606:
	def action(self):
		self.controller.hero.armor += 5
		self.controller.draw()


# Inner Rage
class EX1_607:
	def action(self, target):
		target.buff("EX1_607e")
		self.hit(target, 1)

class EX1_607e:
	Atk = 2
