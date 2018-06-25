import json
import os

filename = "save.json"

class Player(object):
	saveExists = os.path.exists(filename) and os.path.isfile(filename)

	# on Player creation (add args superceding self), set player stats
	def __init__(self, stats, gold, inventory, equipment):
		# or statements add default values to player class when they are new and/or dont have a save file
		self.stats = stats or (
		    1, # 0 level
			2, # 1 defense
			2, # 2 strength
		    2, # 3 speed
		    2, # 4 intelligence
		    0 # 5 experience
		)
		self.battlestats = self.stats
		self.health = 10 * self.stats[0] + 5 * self.stats[2] # 10xLVL + 5xSTR
		self.total_health = self.health
		self.mana = round(self.stats[4] * 2.5) # 250% INT scaling
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
		self.data = { # save data
		    "save":{
		        "stats":self.stats,
		        "health":self.total_health,
		        "mana":self.total_mana,
		        "gold":self.gold,
		        "inventory":self.inventory,
		        "equipment":self.equipment
		    }
		}

	def heal(self, amount):
		if amount >= self.health:
			self.health = self.total_health
		else:
			self.health += amount

		self.update()

	def damage(self, amount):
		if amount >= self.health:
			self.health = 0
		else:
			self.health -= amount

		self.update()

	"""
	In Pokemon, whenever your Pokemon is below it's max health and it levels up, the current health is increased by the DIFFERENCE of the new health and the original (originally current) health. The same can be done in this instance and with both points (health AND mana). Additionally, if there is no difference, the original health becomes the value of the total health, giving the stats a cleaner feel despite the attention to a rather minor detail (for some, it may seem that way).

	This is unnecessary to GAME PERFORMANCE, this was purely done for visual aesthetics.
	"""
	def update(self):
		hp = self.health # old hp
		mp = self.mana # old mana

		self.health = 10 * self.stats[0] + 5 * self.stats[2] # newly generated health
		self.total_health = self.health # newly generated totals
		self.mana = round(self.stats[4] * 2.5) # newly generated mana
		self.total_mana = self.mana

		self.health -= hp # scale hp with "level up"
		self.mana -= mp # scale mp with "level up"
		del hp # garbage collection
		del mp

	def save(self):
		self.data = { # save current player stats in data
		    "save":{
		        "stats":self.stats,
		        "gold":self.gold,
		        "inventory":self.inventory,
		        "equipment":self.equipment
		    }
		}

		with open(filename, "w") as f: # open save file
			self.json = json.dumps(self.data, sort_keys=True, indent=4) # temporary variable for later use in load function (if ever called)
			f.write(self.json)

	def load(self):
		with open(filename, "r") as f:
			json_data = f.read() # read save file content
			self.data = json.loads(json_data) # process it into dict

			# setting player stats through save file dict values
			self.stats,
			self.gold,
			self.inventory,
			self.equipment = tuple(self.data["save"].values()) # static

			# dynamic - highly variable
			self.battlestats = self.stats
			self.health = 10 * self.stats[0] + 5 * self.stats[2]
			self.total_health = self.health
			self.mana = round(self.stats[4] * 2.5)
			self.total_mana = self.mana

# # testing
# print("Run #1\n")
# player = Player(*[None]*4) # default values override None, None == False
# print("health =", player.total_health)
# player.save() # save player data
# # os.startfile(filename)
# player.load() # load player data to make sure it was saved (future removal)
# data = player.data["save"].items()
# for i, v in enumerate(data): # wanted the index
	# k, v = v # v carries (k, v)

	# print(k, "=", v, "\n" if i + 1 == len(data) else "") # check kv pairs

# print("\nRun #2\n")
# player.stats = [69]*6 # stats changed
# player.update() # stats must be updated
# print("health =", player.total_health) # health changes according to health formula
# player.save()
# player.load()
# data = player.data["save"].items()
# for i, v in enumerate(data):
	# k, v = v

	# print(k, "=", v, "\n" if i + 1 == len(data) else "")
