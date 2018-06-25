# Reference
# (
    # 1, # 0 level
    # 2, # 1 defense
    # 2, # 2 strength
    # 2, # 3 speed
    # 2, # 4 intelligence
    # 0 # 5 experience
# )

import random

effects = ( # existing effects for validation
    "heal",
    "damage",
    "poison",
    "burn",
    "teleport"
)

weapon_types = (
    "Unarmed",
    "Sword",
    "Dagger",
    "Greatsword",
    "Spear",
    "Axe"
)

armor_types = (
    "Cloth",
    "Helmet",
    "Armguards",
    "Chestplate",
    "Leggings",
    "Greaves"
)

accessory_types = (
    "Ring",
    "Necklace",
    "Belt"
)

# wip
# abilities = (
    # ("Super Slash", "sword", (("strength", 2.5)), "spins through the enemies!") # move_name, item_name, multiplier(s) (stat, value_to_multi), move_description
# )

weapons = {
    "Unarmed":{
        Weapon(
            name="Leftie",
            stats=[0]*5,
            price=0,
            rarity=0,
            rarity_percentage=0,
            count=0,
            desc="Your trusty left hand, been there through some rather questionable negotiations.",
            descriptor="gives the enemy a 2 without the 1 - a double special!",
            damage=1,
            dual_wieldable=False,
            weapon_type="Unarmed"
        ),

        Weapon(
            name="Rightie",
            stats=[0]*5,
            price=0,
            rarity=0,
            rarity_percentage=0,
            count=0,
            desc="The infamous right hand man - your favorite weapon to use when tussling with the trouble in your trousers. Bring extra paper tissues...",
            descriptor="gives the enemy a solid right hook to the jaw! How do you like them apples? ",
            damage=1,
            dual_wieldable=False,
            weapon_type="Unarmed"
        )
    },

    "Sword":{
        Weapon(
            name="Wooden Sword",
            stats=[1, 0, 1, 2, -2],
            price=10,
            rarity=0,
            rarity_percentage=0,
            count=0,
            desc="It may not be the best (or the sharpest), but in your eyes it's the weilder that makes it great. Maybe that sounded better in your head...",
            descriptor="clobs the enemy, take that you fiendish buffoon! ",
            damage=2,
            dual_wieldable=True,
            weapon_type="Sword"
        )
    },

    "Dagger":None,
    "Greatsword":None,
    "Spear":None,
    "Axe":None
}


class Item(object):
	def __init__(self, name, stats, price, rarity, rarity_percentage, count, desc):
		self.name = name
		self.stats = stats
		self.price = price
		self.sell_price = price / 2 # half original price
		self.rarity = rarity
		self.rarity_percentage = rarity_percentage
		self.count = count
		self.desc = desc
		self.dropped = False

	def try_to_drop(self): # please for the love of god change this function name at some point
		lottery = random.randint(0, 100)

		if lottery <= self.rarity:
			self.dropped = True

class Weapon(Item):
	def __init__(self, name, stats, price, rarity, rarity_percentage, count, desc, descriptor, damage, dual_wieldable, weapon_type):
		super().__init__(name, stats, price, rarity, rarity_percentage, count, desc)
		self.descriptor = descriptor
		self.damage = damage
		self.dual_wieldable = dual_wieldable
		self.weapon_type = weapon_type

class Armor(Item):
	def __init__(self, name, stats, price, rarity, rarity_percentage, count, desc, enchantments, armor_type):
		super().__init__(name, stats, price, rarity, rarity_percentage, count, desc)
		self.enchantments = enchantments # wip
		self.armor_type = armor_type # wip

class Accessory(Item):
	def __init__(self, name, stats, price, rarity, rarity_percentage, count, desc, enchantments, accessory_type):
		super().__init__(name, stats, price, rarity, rarity_percentage, count, desc)

class Potion(Item): # argument allows Potion to inherit off of item
	def __init__(self, name, stats, price, rarity, rarity_percentage, count, desc, effect, effect_value):
		super().__init__(name, stats, price, rarity, rarity_percentage, count, desc) # inheriting class parameters from Item to this class
		self.effect = (effect or None, effect and effect_value or None)
