import os
from time import sleep
import random

### Inventory ###
inventory_list = []

### Default crate values ###
starting_crate_num = 0
basic_crate_num = 0
rare_crate_num = 0
ultra_rare_crate_num = 0
epic_crate_num = 0

### Game items classes ###
class Starter():

	starter_inventory = []

	def list_items():
		for i in Starter.starter_inventory:
			print(i)

	def __init__(self, item, attack, sell_price, buy_price):
		self.item = item
		self.attack = attack
		self.sell_price = sell_price
		self.buy_price = buy_price

		def __str__(self):
			return f"self.item"


class Basic():
	def __init__(self, item, attack, sell_price, buy_price):
		self.item = item
		self.attack = attack
		self.sell_price = sell_price
		self.buy_price = buy_price
	
class Rare():
	def __init__(self, item, attack, sell_price, buy_price):
		self.item = item
		self.attack = attack
		self.sell_price = sell_price
		self.buy_price = buy_price

class UltraRare():
	def __init__(self, item, attack, sell_price, buy_price):
		self.item = item
		self.attack = attack
		self.sell_price = sell_price
		self.buy_price = buy_price

class Epic():
	def __init__(self, item, attack, sell_price, buy_price):
		self.item = item
		self.attack = attack
		self.sell_price = sell_price
		self.buy_price = buy_price


### Game Items ###
# Starter items
starter_sword = Starter('(Starter) - Sword', 20, 50, 70)
starter_spear = Starter('(Starter) - Spear', 15, 25, 30)
starter_gloves = Starter('(Starter) - Gloves', 5, 8, 10)
starter_knife = Starter('(Starter) - Knife', 10, 25, 35)

# Basic Items
basic_gloves = Basic('(Basic) - Gloves', 15, 50, 60)
basic_sword = Basic('(Basic) - Sword', 40, 100, 130)
basic_spear = Basic('(Basic) - Spear', 30, 50, 60)
basic_knife = Basic('(Basic) - Knife', 20, 25, 35)
bear_claws = Basic('(Basic) - Bear Claws', 25, 15, 45)
basic_club = Basic('(Basic) - Club', 0, 0, 0)
brass_knuckles = Basic('(Basic) - Brass Knuckles', 0, 0, 0)

# Rare items
rare_gloves = Rare('(Rare) - Gloves', 30, 16, 20)
rare_sword = Rare('(Rare) - Sword', 80, 200, 260)
rare_spear = Rare('(Rare) - Spear', 60, 100, 120)
rare_knife = Rare('(Rare) - Knife', 40, 50, 70)
rare_short_sword = Rare('(Rare) - Short Sword', 0, 0, 0) 
rare_battle_axe = Rare('(Rare) - Battle Axe', 0, 0 ,0)
rare_mace = Rare('(Rare) - Mace', 0, 0, 0)
morning_star = Rare('(Rare) - Morning Star', 0, 0, 0)
katana = Rare('(Rare) - Katana', 0, 0, 0)


# Ultra rare items
ultra_rare_sword = UltraRare('(Ultra Rare) - Sword', 300, 1800, 2000)
ultra_rare_gloves = UltraRare('(Ultra Rare) - Gloves', 60, 32, 40)
ultra_rare_spear = UltraRare('(Ultra Rare) - Spear', 120, 200, 240)
ultra_rare_knife = UltraRare('(Ultra Rare) - Knife', 80, 100, 140)
war_hammer = UltraRare('(Ultra Rare) - War Hammer', 0, 0, 0) 
war_scythe = UltraRare('(Ultra Rare) - War Scythe', 0, 0, 0)


# Epic Items
epic_energy_sword = Epic('(Epic) - Energy Sword', 1000, 80000, 100000)
magic_wand = Epic('(Epic) - Magic Wand', 700, 1000, 1200)


### Crate containers ###
starting_crate = [starter_sword, starter_spear, starter_gloves, starter_knife]
basic_crate = [basic_gloves, basic_sword, basic_spear, basic_knife, bear_claws, basic_club, brass_knuckles,]
rare_crate = [rare_gloves, rare_sword, rare_spear, rare_battle_axe, rare_mace, morning_star, katana, rare_short_sword]
ultra_rare_crate = [ultra_rare_sword, ultra_rare_spear, ultra_rare_knife, ultra_rare_gloves, war_hammer, war_scythe]
epic_crate = [epic_energy_sword, magic_wand]

### Start. run before everything ###
print('-------------------------------------------------------')
print('|    ...before we begin, please enter your name...    |')
print('-------------------------------------------------------')
name = input('> ')
money = 0
player = {"name": name, }
os.system('clear')

### 'Tutorial' + free crate ###
def start(starting_crate_num):
	starting_crate_num += 1
	os.system('clear')
	print('-----------------------------------------')
	print('|    ...You have started the game...    |')
	print('-----------------------------------------')
	sleep(1.5)
	os.system('clear')
	print("To start you off, you're given a basic crate!")
	print('Would you like to view your current crates?')
	print('(1) Yes')
	print('(2) No')
	answer = input("> ")

	if answer == "1":
		os.system('clear')
		print('TIP:')
		print("""           ...To open a crate, you need to select it...
...Type the corresponding number and it will open that crate!...""")
		sleep(4)
		os.system('clear')
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)
	elif answer == "2":
		pass
	else:
		pass

def available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num):
	os.system('clear')
	print('------------------------------')
	print('|   ...Available crates...   |')
	print('------------------------------')
	if starting_crate_num > 0:
		print('\n1: Starter crates: ' + '(' + str(starting_crate_num) + ')')
	else:
		print('\n1: Starter crates: ' + '(' + str(starting_crate_num) + ')')

	if basic_crate_num > 0:
		print('\n2: Basic crates: ' + '(' + str(basic_crate_num) + ')')
	else:
		print('\n2: Basic crates: ' + '(' + str(basic_crate_num) + ')')

	if rare_crate_num > 0:
		print('\n3: Rare crates: ' + '(' + str(rare_crate_num) + ')')
	else:
		print('\n3: Rare crates: ' + '(' + str(rare_crate_num) + ')')

	if ultra_rare_crate_num > 0:
		print('\n4: Ultra rare crates: ' + '(' + str(ultra_rare_crate_num) + ')')
	else:
		print('\n4: Ultra rare crates: ' + '(' + str(ultra_rare_crate_num) + ')')

	if epic_crate_num > 0:
		print('\n5: Epic crates: ' + '(' + str(epic_crate_num) + ')')
	else:
		print('\n5: Epic crates: ' + '(' + str(epic_crate_num) + ')')

	open_crate = input('> ')
	if open_crate == "1" and starting_crate_num != 0:
		starting_crate_num -= 1
		randomed_crate = random.choice(starting_crate)
		os.system('clear')
		print("You opened Starter Crate and got '{}'".format(randomed_crate.item) + '!')
		inventory_list.append(randomed_crate)
		sleep(2.5)
		os.system('clear')
		print('-----------------------------------------')
		print('|    Where would you like to go now?    |')
		print('-----------------------------------------')
		print('(1) Main Menu')
		print('(2) Available Crates')
		answer = input('> ')

		if answer == "1":
			main_menu()
		if answer == "2":
			os.system('clear')
			available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "2" and basic_crate_num != 0:
		basic_crate_num -= 1
		randomed_crate = random.choice(basic_crate)
		os.system('clear')
		print("You opened Basic Crate and got '{}'".format(randomed_crate.item) + '!')
		inventory.append(randomed_crate)
		sleep(2.5)
		os.system('clear')
		print('-----------------------------------------')
		print('|    Where would you like to go now?    |')
		print('-----------------------------------------')
		print('(1) Main Menu')
		print('(2) Available Crates')
		answer = input('> ')

		if answer == "1":
			main_menu()
		if answer == "2":
			os.system('clear')
			available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)


	elif open_crate == "3" and rare_crate_num != 0:
		rare_crate_num -= 1
		randomed_crate = random.choice(rare_crate)
		os.system('clear')
		print("You opened Rare Crate and got '{}'".format(randomed_crate.item) + '!')
		inventory.append(randomed_crate)
		sleep(2.5)
		os.system('clear')
		print('-----------------------------------------')
		print('|    Where would you like to go now?    |')
		print('-----------------------------------------')
		print('(1) Main Menu')
		print('(2) Available Crates')
		answer = input('> ')

		if answer == "1":
			main_menu()
		if answer == "2":
			os.system('clear')
			available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "4" and ultra_rare_crate_num != 0:
		ultra_rare_crate_num -= 1
		randomed_crate = random.choice(ultra_rare_crate)
		os.system('clear')
		print("You opened an Ultra Rare Crate and got '{}'".format(randomed_crate.item) + '!')
		inventory.append(randomed_crate)
		sleep(2.5)
		os.system('clear')
		print('-----------------------------------------')
		print('|    Where would you like to go now?    |')
		print('-----------------------------------------')
		print('(1) Main Menu')
		print('(2) Available Crates')
		answer = input('> ')

		if answer == "1":
			main_menu()
		if answer == "2":
			os.system('clear')
			available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "5" and epic_crate_num != 0:
		epic_crate_num -= 1
		randomed_crate = random.choice(epic_crate)
		os.system('clear')
		print("You opened an Epic Crate and got '{}'".format(randomed_crate.item) + '!')
		item = "{}".format(randomed_crate.item)
		inventory.append(item)
		sleep(2.5)
		os.system('clear')
		print('-----------------------------------------')
		print('|    Where would you like to go now?    |')
		print('-----------------------------------------')
		print('(1) Main Menu')
		print('(2) Available Crates')
		answer = input('> ')

		if answer == "1":
			main_menu()
		if answer == "2":
			os.system('clear')
			available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "menu":
		main_menu()

	elif open_crate == "chtstarter":
		starting_crate_num += 1
		os.system('clear')
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "chtbasic":
		basic_crate_num += 1
		os.system('clear')
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "chtrare":
		rare_crate_num += 1
		os.system('clear')
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "chtultrarare":
		ultra_rare_crate_num += 1
		os.system('clear')
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	elif open_crate == "chtepic":
		epic_crate_num += 1
		os.system('clear')
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

	else:
		os.system('clear')
		print("""Invalid, you either don't have enough of the selected crate,
or ou didn't type the corresponding number.""")
		print("Please type 'menu' to go to the main menu")
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)

def info():
	os.system('clear')
	print("...Welcome to Info!...")
	print("""To play, you have to go on quests, while on quests,
you have a chance to find a crate. but, you also have a chance
of finding an enemy. If you don't have a weapon that is capable
of defeating that enemy, you die and lose all items you own.
You can decide the levels of quest you want to go on, and the more You
progress, the harder difficulty of quest you can go on. The higher level
your character is, you can complete quests faster, and you become stronger.
If you find a crate, you can find random items inside, depending on the quest,
and what level of crate it is, you can get better or worse items.""")
	print('------------------------------------------')
	print("Please type '1' to go back to the main menu!")
	start = input('> ')

	if start == "1":
		start()
	else:
		print("Invalid, please type '1'")
		info()

def tips():
	os.system('clear')
	tips = ["If you're in available crates, simply type 'menu' to come to the main menu!",]
	print(random.choice(tips))
	sleep(6)
	main_menu

def inventory():
	print(Starter.list_items)

def main_menu():
	os.system('clear')
	print('-----------------------------------------')
	print('|    ...Welcome to the Main Menu!...    |')
	print('-----------------------------------------')
	print('(1) Start a Quest')
	print('(2) Available Crates')
	print('(3) Inventory')
	print('(4) Info')
	print('(5) Shop')
	print('(6) Tips')
	answer = input('> ')
	
	if answer == "1":
		pass
	elif answer == "2":
		available_crates(starting_crate_num, basic_crate_num, rare_crate_num, ultra_rare_crate_num, epic_crate_num)
	elif answer == "3":
		inventory()
	elif answer == "4":
		info()
	elif answer == "5":
		pass
	elif answer == "6":
		tips()
	else:
		print('Invalid, please type the corresponding number. ')
		main_menu()

### CHEATS ###
### Used in the available crates section ###
#chtall = gives 1 of all crates
#chtstarter = gives 1 starter crate
#chtbasic = gives 1 basic crate
#chtrare = gives 1 rare crate
#chtultrarare = gives 1 ultra rare crate      
#chtepic = gives 1 epic crate


start(starting_crate_num)
