##
# Minions

# Webspinner
class FP1_011:
	def deathrattle(self):
		self.controller.give(random.choice(self.data.entourage))


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


# Anub'ar Ambusher
class FP1_026:
	def deathrattle(self):
		if self.controller.field:
			random.choice(self.controller.field).bounce()


##
# Spells

# Reincarnate
class FP1_025:
	def action(self, target):
		target.destroy()
		self.controller.summon(target.id)
