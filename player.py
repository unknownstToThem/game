import json
import os

filename = "save.json"

class Player(object):
	saveExists = os.path.exists(filename) and os.path.isfile(filename)

	# on Player creation (add args superceding self), set player stats
	def __init__(self, stats, gold, inventory, equipment):
		self.stats = stats or (
		    1, # 0 level
			2, # 1 defense
			2, # 2 strength
		    2, # 3 speed
		    2, # 4 intelligence
		    0 # 5 experience
		)
		self.battlestats = self.stats
		self.health = 10 * stats[0] + 5 * stats[2] # 10xLVL + 5xSTR
		self.total_health = self.health
		self.mana = round(stats[4] * 2.5)
		self.total_mana = self.mana
		self.gold = gold or 0
		self.inventory = inventory or []
		self.equipment = equipment or (
			"Leftie", # left handed weapon
			"Rightie", # right handed weapon
			None, # helmet
			None, # armguards
			None, # chestplate
		    None, # leggings
			None, # greaves
			None # accessory
		)

	def save():
		self.data = json.dumps({
		    "stats":self.stats,
		    "health":self.total_health,
		    "mana":self.total_mana,
		    "gold":self.gold,
		    "inventory":self.inventory,
		    "equipment":self.equipment
		})

		with open(filename, "w") as f:
			json.dump(self.data, f)

	def load():
		if saveExists:
			with open(filename, "r") as f:
				json_data = f.read()
				self.data = json.loads(json_data)[0]


