import random
from player import *
from items import *

"""
Import items
Stick items in indexed lottery
Random gen number in lottery
Item with number == index is the drop
Item format: (itemObj, drop_chance)
Item: (Sword(), 10) for 10% chance
Random gen number
If number <= 10, return sword
Else, return None
Random gen number in other_drop
if other_drop <= n, repeat
Can only have max of 3 drops, 2 being weapons, 1 being either an accessory or potion
"""

class Enemy(Player):
	def __init__(self, stats, gold, inventory, equipment, drop):
		super().__init__(self, stats, gold, inventory, equipment)
		can_drop = random.randint(0,100) <= 5

		if can_drop: # only weapons-drops as weapons have only been made
			item
