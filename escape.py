from math import *
from kandinsky import *
from ion import *
from time import *

def deepcopy(obj, memo=None):
    if memo is None:
        memo = {}

    obj_id = id(obj)

    if obj_id in memo:
        return memo[obj_id]
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj

    if isinstance(obj, list):
        copy_list = [deepcopy(item, memo) for item in obj]
        memo[obj_id] = copy_list
        return copy_list

    if isinstance(obj, tuple):
        copy_tuple = tuple(deepcopy(item, memo) for item in obj)
        memo[obj_id] = copy_tuple
        return copy_tuple

    if isinstance(obj, dict):
        copy_dict = {deepcopy(key, memo): deepcopy(value, memo) for key, value in obj.items()}
        memo[obj_id] = copy_dict
        return copy_dict

    if isinstance(obj, set):
        copy_set = {deepcopy(item, memo) for item in obj}
        memo[obj_id] = copy_set
        return copy_set

    if hasattr(obj, "__dict__"):
        copy_obj = obj.__class__.__new__(obj.__class__)
        memo[obj_id] = copy_obj
        for key, value in obj.__dict__.items():
            setattr(copy_obj, key, deepcopy(value, memo))
        return copy_obj

background_color = color(255, 255, 255)
character_color = color(0, 0, 200)
block_color = color(200, 200, 200)
shadow_block_color = color(145, 145, 145)
grass_color = color(0, 255, 0)
spike_block_color = color(100, 100, 100)
shadow_coin_color = color(255, 183, 52)
coin_color = color(255, 255, 0)
spike_color = color(255, 0, 0)
shadow_spike_color = color(200, 0, 0)
start_color = color(0, 200, 200)
end_color = color(200, 0, 200)

# '0' : void
# '1' : block
# '2' : coin
# '3' : spike
# '4' : start
# '5' : end
# '6' : spike block
maps = {"Niveau 1": [
['3', '3', '3', '5', '3', '3', '1', '3', '3', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
['3', '0', '1', '0', '0', '1', '0', '0', '0', '2', '2', '1', '1', '0', '0', '1', '0', '1', '0', '3'],
['1', '2', '2', '0', '0', '1', '2', '0', '0', '0', '0', '2', '1', '0', '0', '0', '0', '2', '2', '1'],
['3', '0', '0', '0', '0', '1', '1', '3', '3', '3', '0', '0', '1', '0', '0', '2', '0', '1', '0', '3'],
['3', '2', '0', '0', '1', '1', '2', '0', '0', '0', '0', '2', '1', '1', '0', '0', '0', '0', '2', '3'],
['3', '1', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1', '1', '2', '0', '0', '0', '0', '2', '3'],
['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '3'],
['2', '0', '2', '1', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3'],
['1', '0', '0', '0', '0', '1', '0', '2', '0', '2', '0', '2', '0', '2', '0', '0', '0', '0', '0', '3'],
['3', '0', '0', '0', '0', '1', '3', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '2', '0', '3'],
['3', '2', '0', '0', '2', '1', '2', '0', '0', '0', '0', '2', '1', '0', '0', '0', '1', '2', '0', '3'],
['3', '2', '0', '1', '2', '1', '2', '0', '0', '0', '2', '0', '1', '2', '1', '2', '1', '2', '0', '3'],
['1', '0', '0', '2', '2', '1', '0', '2', '2', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '3'],
['1', '1', '1', '3', '3', '3', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3']],
"Niveau 2": [
['3', '0', '1', '0', '1', '3', '0', '3', '3', '0', '0', '1', '3', '1', '3', '1', '0', '0', '0', '2'],
['3', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '3', '1', '0', '0', '1', '1'],
['3', '0', '2', '0', '2', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '5'],
['0', '0', '2', '1', '1', '0', '0', '2', '0', '1', '2', '1', '1', '0', '0', '0', '0', '0', '0', '0'],
['0', '1', '0', '0', '0', '0', '1', '0', '1', '3', '0', '0', '2', '0', '1', '2', '0', '0', '0', '0'],
['3', '0', '0', '0', '1', '0', '1', '0', '2', '1', '1', '0', '0', '0', '0', '2', '1', '0', '0', '2'],
['1', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '2', '2', '0', '0', '0'],
['4', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1'],
['1', '0', '0', '0', '2', '3', '1', '2', '0', '1', '0', '2', '1', '0', '0', '0', '1', '0', '0', '1'],
['0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '2', '1', '0', '0', '0', '0', '0', '0', '0', '2'],
['0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '0', '0', '3', '1', '0', '3', '1', '0', '0'],
['1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '2', '0', '0', '0', '0', '1', '1', '1', '0', '1'],
['2', '1', '0', '0', '0', '0', '1', '0', '0', '1', '2', '0', '0', '0', '0', '1', '3', '0', '0', '3'],
['0', '0', '2', '0', '1', '2', '3', '0', '3', '1', '3', '1', '1', '1', '1', '3', '0', '0', '2', '3']],
"Niveau 3": [
['2', '0', '2', '6', '0', '3', '3', '0', '6', '0', '3', '3', '0', '3', '3', '0', '3', '3', '0', '0'],
['2', '3', '0', '0', '2', '2', '0', '6', '0', '0', '0', '2', '0', '0', '2', '0', '0', '2', '0', '6'],
['0', '0', '6', '6', '0', '3', '2', '6', '0', '0', '6', '0', '3', '0', '6', '0', '0', '2', '2', '5'],
['0', '2', '0', '2', '6', '0', '2', '6', '0', '3', '2', '2', '2', '6', '0', '0', '0', '0', '6', '0'],
['0', '0', '3', '0', '3', '0', '6', '0', '2', '1', '2', '0', '0', '0', '0', '2', '0', '0', '3', '0'],
['0', '6', '0', '2', '3', '0', '0', '2', '6', '0', '0', '6', '2', '0', '2', '1', '3', '0', '3', '0'],
['4', '2', '6', '2', '3', '6', '0', '6', '0', '2', '2', '0', '6', '0', '0', '0', '0', '2', '6', '2'],
['3', '0', '0', '0', '3', '3', '0', '3', '0', '3', '3', '0', '3', '0', '6', '0', '3', '0', '0', '2'],
['3', '2', '0', '0', '0', '6', '0', '0', '0', '0', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
['3', '2', '0', '2', '6', '0', '0', '0', '6', '3', '3', '0', '0', '3', '3', '3', '0', '6', '6', '0'],
['3', '0', '6', '2', '0', '3', '0', '0', '2', '2', '6', '0', '0', '6', '0', '0', '0', '3', '2', '2'],
['3', '0', '0', '0', '0', '0', '6', '6', '0', '0', '1', '2', '2', '0', '0', '0', '6', '0', '0', '3'],
['3', '2', '0', '0', '2', '6', '6', '0', '0', '2', '0', '6', '3', '0', '3', '0', '3', '3', '0', '3'],
['0', '6', '0', '0', '6', '3', '3', '2', '3', '6', '0', '0', '0', '0', '6', '0', '0', '0', '0', '6']]}

def search_start():
	for y in range(14):
		for x in range(20):
			if actualMap[y][x] == '4':
				return [x, y]

class Character:
	def __init__(self):
		self.pos = [0, 0]
		self.coins = 0

	def erase_position(self, x, y):
		fill_rect(x * 16 + 1, y * 16 + 1, 14, 14, background_color)
		if actualMap[y][x] == '5':
			draw_end(x, y)

	def show(self):
		fill_rect(self.pos[0] * 16 + 1, self.pos[1] * 16 + 1, 14, 14, character_color)

	def up(self):
		self.erase_position(self.pos[0], self.pos[1])
		for y in range(self.pos[1] - 1, -1, -1):
			if self.move(self.pos[0], y, 'u') == 1:
				break

		self.show()

	def down(self):
		self.erase_position(self.pos[0], self.pos[1])
		for y in range(self.pos[1] + 1, 14, 1):
			if self.move(self.pos[0], y, 'd') == 1:
				break

		self.show()

	def left(self):
		self.erase_position(self.pos[0], self.pos[1])
		for x in range(self.pos[0] - 1, -1, -1):
			if self.move(x, self.pos[1], 'l') == 1:
				break

		self.show()

	def right(self):
		self.erase_position(self.pos[0], self.pos[1])
		for x in range(self.pos[0] + 1, 20, 1):
			if self.move(x, self.pos[1], 'r') == 1:
				break

		self.show()

	def move(self, x, y, d):
		global running

		if actualMap[y][x] == '2':
			actualMap[y][x] = '0'
			self.coins += 1
			self.erase_position(x, y)
		elif actualMap[y][x] == '1' or actualMap[y][x] == '6':
			if d == 'd':
				self.pos[1] = y - 1
			if d == 'u':
				self.pos[1] = y + 1
			if d == 'r':
				self.pos[0] = x - 1
			if d == 'l':
				self.pos[0] = x + 1
			if actualMap[y][x] == '6':
				actualMap[y][x] = '3'
				erase_position(x, y)
				draw_spike(x * 16, y * 16)
				sleep(0.2)
			return 1
		elif actualMap[y][x] == '3':
			running = None
			return 1
		elif actualMap[y][x] == '5':
			coinFound = False
			for Y in range(14):
				for X in range(20):
					if actualMap[Y][X] == '2':
						coinFound = True
						break

			if coinFound == False:
				running = False
			else:
				self.pos = [x, y]
			return 1
		elif (x == 0 and d == 'l') or (x == 19 and d == 'r'):
			self.pos[0] = x
			return 1
		elif (y == 0 and d == 'u') or (y == 13 and d == 'd'):
			self.pos[1] = y
			return 1

def clear_screen():
	fill_rect(0, 0, 320, 226, background_color)

def erase_position(x, y):
	fill_rect(x * 16, y * 16, 16, 16, background_color)

def draw_block(X, Y, x, y, scale = 2):
	t_start, b_start = 1, 1
	t_end, b_end = 0, 0
	extended_down = 0
	extended_left = 0

	if X > 0:
		if actualMap[Y][X - 1] == '1' or actualMap[Y][X - 1] == '6':
			t_start = 0
			b_start = 0
			extended_left = 1
	if X < 19:
		if actualMap[Y][X + 1] == '1' or actualMap[Y][X + 1] == '6':
			t_end = 1
			b_end = 1
	if Y > 0:
		if actualMap[Y - 1][X] == '1' or actualMap[Y - 1][X] == '6':
			t_start = 0
			t_end = 1
	if Y < 13:
		if actualMap[Y + 1][X] == '1' or actualMap[Y + 1][X] == '6':
			b_start = 0
			b_end = 1
			extended_down = 1

	fill_rect(x + t_start * scale, y, (7 - t_start + t_end) * scale, scale, grass_color)
	if extended_down == 0:
		if extended_left == 0:
			fill_rect(x, y + 3 * scale, scale, 4 * scale, shadow_block_color)
		fill_rect(x + (1 - extended_left) * scale, y + 3 * scale, (7 + extended_left) * scale, 4 * scale, block_color)
		fill_rect(x + b_start * scale, y + 7 * scale, (7 - b_start + b_end) * scale, scale, block_color)
	fill_rect(x, y + 1 * scale, 8 * scale, (2 + 4 * extended_down) * scale, grass_color)
	fill_rect(x + b_start * scale, y + (3 + 4 * extended_down) * scale, (7 - b_start + b_end) * scale, scale, grass_color)

def draw_end(x, y, scale = 2):
	fill_rect(x + 2 * scale, y + 2 * scale, 4 * scale, 4 * scale, end_color)

def draw_coin(x, y, scale = 2):
	fill_rect(x + 3 * scale, y + 2 * scale, 2 * scale, 4 * scale, coin_color)
	fill_rect(x + int(3.5 * scale), y + 3 * scale, scale, 2 * scale, shadow_coin_color)

def draw_spike(x, y, scale = 2):
	fill_rect(x + int(3.5 * scale), y + 2 * scale, int(0.5 * scale), scale, shadow_spike_color)
	fill_rect(x + 4 * scale, y + 2 * scale, int(0.5 * scale), scale, spike_color)

	fill_rect(x + 3 * scale, y + 3 * scale, scale, scale, shadow_spike_color)
	fill_rect(x + 4 * scale, y + 3 * scale, scale, scale, spike_color)

	fill_rect(x + int(2.5 * scale), y + 4 * scale, scale, scale, shadow_spike_color)
	fill_rect(x + int(3.5 * scale), y + 4 * scale, 2 * scale, scale, spike_color)

	fill_rect(x + 2 * scale, y + 5 * scale, scale, scale, shadow_spike_color)
	fill_rect(x + 3 * scale, y + 5 * scale, 3 * scale, scale, spike_color)

	fill_rect(x + int(1.5 * scale), y + 6 * scale, scale, scale, shadow_spike_color)
	fill_rect(x + int(2.5 * scale), y + 6 * scale, 4 * scale, scale, spike_color)

	fill_rect(x + int(2.5 * scale), y + 7 * scale, 3 * scale, int(0.5 * scale), spike_color)

def draw_start(x, y, scale = 2):
	fill_rect(x + 2 * scale, y + 2 * scale, 4 * scale, 4 * scale, start_color)

def show_dead():
	fill_rect(0, 0, 320, 226, color(0, 0, 0))
	draw_string("Vous êtes mort !", 75, 100)
	draw_string("Appuyez sur OK pour continuer", 15, 200)
	while not keydown(KEY_OK):
		pass

def show_victory(levelTime):
	clear_screen()
	draw_string("Vous avez terminé !", 60, 50)
	draw_string("En {:.2f}".format(int(levelTime * 100) / 100) + " s", 20, 100)
	draw_string("Appuyez sur OK pour continuer", 15, 200)
	while not keydown(KEY_OK):
		pass

def show_menu():
	reset()
	show(160, 54, 1, False)
	draw_string("MENU PRINCIPAL", 20, 0)
	draw_string("Appuyez sur OK pour commencer", 15, 200)
	if level != 0:
		draw_string("	" + mapsNames[level - 1].lower(), 20, 60)
	fill_rect(10, 98, 140, 22, grass_color)
	draw_string(mapsNames[level].upper(), 20, 100)
	if level != len(mapsNames) - 1:
		draw_string("	" + mapsNames[level + 1].lower(), 20, 140)

def menu():
	global level
	show_menu()

	while not keydown(KEY_BACK):
		if keydown(KEY_OK):
			sleep(0.3)
			game()
			show_menu()
		if keydown(KEY_UP):
			if level == 0:
				level = len(mapsNames) - 1
			else:
				level -= 1
			sleep(0.2)
			show_menu()
		if keydown(KEY_DOWN):
			if level == len(mapsNames) - 1:
				level = 0
			else:
				level += 1
			sleep(0.2)
			show_menu()

def show(posx = 0, posy = 0, scale = 2, ch = True):
	global actualMap
	clear_screen()

	for Y in range(14):
		for X in range(20):
			x, y = X * 8 * scale + posx, Y * 8 * scale + posy
			if actualMap[Y][X] == '1' or actualMap[Y][X] == '6':
				draw_block(X, Y, x, y, scale)
			elif actualMap[Y][X] == '2':
				draw_coin(x, y, scale)
			elif actualMap[Y][X] == '3':
				draw_spike(x, y, scale)
			elif actualMap[Y][X] == '4':
				draw_start(x, y, scale)
			elif actualMap[Y][X] == '5':
				draw_end(x, y, scale)

	if ch == True:
		character.show()

character = Character()
mapsNames = list(maps.keys())
mapsNames.sort()
level = 0
running = True

def reset():
	global actualMap
	actualMap = deepcopy(maps[mapsNames[level]])
	character.pos = search_start().copy()

def game():
	global running
	reset()
	show(ch = False)
	for i in range(3, 0, -1):
		draw_string(str(i), character.pos[0] * 16 + 4, character.pos[1] * 16 + 1)
		sleep(0.5)
	character.show()
	startTime = monotonic()
	while running == True:
		if keydown(KEY_OK):
			running = None
			sleep(0.3)
		if keydown(KEY_UP):
			character.up()
		elif keydown(KEY_DOWN):
			character.down()
		elif keydown(KEY_RIGHT):
			character.right()
		elif keydown(KEY_LEFT):
			character.left()
	endTime = monotonic()

	if running == None:
		show_dead()
	else:
		show_victory(endTime - startTime)
	running = True
	sleep(0.3)

menu()
