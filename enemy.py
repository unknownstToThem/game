import random
# from items import *

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

class Enemy(object):
	def __init__(self, stats, gold, drop):
		self.stats = stats
		self.gold = 1
		# if random.randint(1,100) <= 5 
