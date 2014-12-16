##
# Minions

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
