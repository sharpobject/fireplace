from fireplace.enums import CardType

# Northshire Cleric
class CS2_235:
	def HEAL(self, source, target, amount):
		if target.type == CardType.MINION:
			self.controller.draw()
