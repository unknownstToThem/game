effects = ( # existing effects for validation
    "heal",
    "damage",
    "poison",
    "burn",
    "teleport"
)

abilities = (
    # ("Super Slash", "sword", (("strength", 2.5)), "spins through the enemies!") # move_name, item_name, multiplier(s) (stat, value_to_multi), move_description
)

armor_types = (
    "Helmet",
    "Armguards",
    "Chestplate",
    "Leggings",
    "Greaves"
)

weapon_types = (
    "Sword",
    "Dagger",
    "Greatsword",
    "Spear",
    "Axe"
)

class Item(object):
	def __init__(self, stats, price, rarity):
		self.stats = stats
		self.price = price
		self.sell_price = price / 2 # half original price

class Potion(Item): # argument allows Potion to inherit off of item
	def __init__(self, stats, price, rarity, effect, effect_value):
		super().__init__(stats, price, rarity) # inheriting class parameters from Item to this class
		self.effect = (effect, effect_value)

class Weapon(Item):
	def __init__(self, stats, price, rarity, damage, descriptor, weapon_type):
		super().__init__(stats, price, rarity)
		self.damage = damage
		self.descriptor = descriptor
		self.weapon_type = weapon_type

class Armor(Item):
	def __init__(self, stats, price, rarity, enchantments, armor_type):
		super().__init__(stats, price, rarity)
