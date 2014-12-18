from ..utils import *

##
# Free basic minions

# Raid Leader
class CS2_122:
	aura = "CS2_122e"

class CS2_122e:
	Atk = 1
	targeting = TARGET_FRIENDLY_MINIONS
	def isValidTarget(self, target):
		return target is not self.source


# Frostwolf Warlord
class CS2_226:
	def action(self):
		for target in self.controller.field:
			self.buff("CS2_226e")

class CS2_226e:
	Atk = 1
	Health = 1

# RFG: Has +1/+1 for each other friendly minion on the battlefield.
# class CS2_226o:
#	pass


# Voodoo Doctor
class EX1_011:
	action = healTarget(2)


# Novice Engineer
class EX1_015:
	action = drawCard


# Demolisher
class EX1_102:
	def OWN_TURN_BEGIN(self):
		self.hit(random.choice(self.controller.getTargets(TARGET_ENEMY_CHARACTERS)), 2)


# Arathi Weaponsmith
class EX1_398:
	def action(self):
		self.controller.summon("EX1_398t")


# Gurubashi Berserker
class EX1_399:
	def SELF_DAMAGE(self, amount, source):
		self.buff("EX1_399e")

class EX1_399e:
	Atk = 3


# Nightblade
class EX1_593:
	action = damageEnemyHero(3)


# Cult Master
class EX1_595:
	def OWN_MINION_DESTROYED(self, minion):
		self.controller.draw()


##
# Common basic minions

# Earthen Ring Farseer
class CS2_117:
	action = healTarget(3)


# Ironforge Rifleman
class CS2_141:
	action = damageTarget(1)


# Gnomish Inventor
class CS2_147:
	action = drawCard


# Stormpike Commando
class CS2_150:
	action = damageTarget(2)


# Silver Hand Knight
class CS2_151:
	action = summonMinion("CS2_152")


# Elven Archer
class CS2_189:
	action = damageTarget(1)


# Abusive Sergeant
class CS2_188:
	action = buffTarget("CS2_188o")

class CS2_188o:
	Atk = 2


# Razorfen Hunter
class CS2_196:
	action = summonMinion("CS2_boar")


# Stormwind Champion
class CS2_222:
	aura = "CS2_222o"

class CS2_222o:
	Atk = 1
	Health = 1
	targeting = TARGET_FRIENDLY_MINIONS
	def isValidTarget(self, target):
		return target is not self.source


# Darkscale Healer
class DS1_055:
	def action(self):
		for target in self.controller.getTargets(TARGET_FRIENDLY_CHARACTERS):
			self.heal(target, 2)


# Acolyte of Pain
class EX1_007:
	SELF_DAMAGE = drawCard


# Shattered Sun Cleric
class EX1_019:
	action = buffTarget("EX1_019e")

class EX1_019e:
	Atk = 1
	Health = 1


# Dragonling Mechanic
class EX1_025:
	action = summonMinion("EX1_025t")


# Leper Gnome
class EX1_029:
	deathrattle = damageEnemyHero(2)


# Dark Iron Dwarf
class EX1_046:
	action = buffTarget("EX1_046e")

class EX1_046e:
	Atk = 2


# Youthful Brewmaster
class EX1_049:
	action = bounceTarget


# Ancient Brewmaster
class EX1_057:
	action = bounceTarget


# Acidic Swamp Ooze
class EX1_066:
	def action(self):
		if self.controller.opponent.hero.weapon:
			self.controller.opponent.hero.weapon.destroy()


# Loot Hoarder
class EX1_096:
	deathrattle = drawCard


# Dire Wolf Alpha
class EX1_162:
	aura = "EX1_162o"

class EX1_162o:
	Atk = 1
	targeting = TARGET_FRIENDLY_MINIONS


# Frost Elemental
class EX1_283:
	def action(self, target):
		target.frozen = True


# Murloc Tidehunter
class EX1_506:
	action = summonMinion("EX1_506a")


# Grimscale Oracle
class EX1_508:
	aura = "EX1_508o"

class EX1_508o:
	targeting = TARGET_FRIENDLY_MINIONS
	Atk = 1
	def isValidTarget(self, target):
		return target.race == Race.MURLOC and target is not self.source


# Harvest Golem
class EX1_556:
	deathrattle = summonMinion("skele21")


# Priestess of Elune
class EX1_583:
	def action(self):
		self.heal(self.controller.hero, 4)


# Flesheating Ghoul
class tt_004:
	def MINION_DESTROYED(self):
		self.buff("tt_004o")

class tt_004o:
	Atk = 1
