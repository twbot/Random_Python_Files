#!/usr/bin/env python3

import random

board = []
board_ends = []
player_pos = []

monster_type = ''

x = 0
y = 0
#print menu at beginning
def menu():
	print('> Welcome to the game!')
	choose_board()
	choose_monster()
		

def choose_board():
	choose_dim = input('> Default board dimensions is 3x3. Press Y for default or N to customize: ').lower()
	if choose_dim == 'n':
		dim = tuple(map(int,input('> Please input number of cells, seperated by a comma (e.g. 3,4): ').split(',')))
		get_dimensions(dim)
	elif choose_dim == 'y':
		get_dimensions((3,3))
	else:
		print('Input invalid. Please enter "Y" or "N"')
		return choose_board()

def choose_monster():
	choose_monster = input('> Monster is static by default. If you would like a dynamic monster, press Y, else press N: ').lower()
	if choose_monster.isalpha():
		global monster_type
		monster_type = choose_monster
	elif not choose_monster.isalpha():
		print('> Input invalic. Please select "Y" or "N".')
		return choose_monster()

#function to make list of ends of board
def ends():
	n_board = board
	num = (y - 1)
	for index, tup in enumerate(n_board):
		if index == num:
			board_ends.append(index)
			num += y


#function to get number of cells in game
def get_dimensions(cells):
	length,width = cells  #length, width
	global x
	x = length
	global y
	y = width
	length_index = 0
	width_index = 0
	for length_index in range(length):
		for width_index in range((width)):
			board.append((length_index, width_index))

#function to print map
def draw_map(player, monster):
	for line in range(y-1):
		print(' _', end = '')
	print(' _ ')
	tile = '|{}'
	for index, cell in enumerate(board):
		if index not in board_ends:
			if cell == player:
				print(tile.format('X'), end = '')
			elif cell == monster:
				print(tile.format('M'), end = '')
			else:
				print(tile.format('_'), end = '')
		else:
			if cell == player:
				print(tile.format('X|'))
			elif cell == monster:
				print(tile.format('M|'))
			else:
				print(tile.format('_|'))

#function to keep track of players moves
#def track_player(player):
	
#function to move player
def move_player(player, move):
	x_player,y_player = player
	if move == 'LEFT':
		y_player -= 1
	elif move == 'RIGHT':
		y_player += 1
	elif move == 'UP':
		x_player -= 1
	elif move == 'DOWN':
		x_player += 1
	return x_player,y_player

#function to move monster
def move_monster(monster, value, moves):
	if value == 1:
		x_monster,y_monster = monster
		move = random.choice(moves)
		if move == 'LEFT':
			y_monster -= 1
		elif move == 'RIGHT':
			y_monster += 1
		elif move == 'UP':
			x_monster -= 1
		elif move == 'DOWN':
			x_monster += 1
		return x_monster,y_monster
	else:
		pass

#function to keep track of available moves
def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	if player[1] == 0:
		moves.remove('LEFT')
	if player[1] == (y-1):
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == (x-1):
		moves.remove('DOWN')
	return moves

def get_moves_monster(monster, value):
	if value == 1:
		moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
		if monster[1] == 0:
			moves.remove('LEFT')
		if monster[1] == (y-1):
			moves.remove('RIGHT')
		if monster[0] == 0:
			moves.remove('UP')
		if monster[0] == (x-1):
			moves.remove('DOWN')
		return moves
	else:
		pass

#function to get starting positions of player, monster, and door
def get_positions():
	player = random.choice(board)
	monster = random.choice(board)
	door = random.choice(board)
	if door == player or door == monster or monster == player:
		return get_positions()
	return player, monster, door

def main():
	menu()
	ends()
	player, monster, door = get_positions()
	value = 0
	if monster_type == 'y':
		value = 1
	while True:
		print()
		print('You are currently in position {}'.format(player))  #fill in with player position
		moves = get_moves(player)
		moves_monster = get_moves_monster(monster, value)
		draw_map(player, monster)
		print('You can move {}'.format(moves))  #fill in with available moves
		print('Enter QUIT to quit.')
		move = input('>  ')
		move = move.upper()
		if move == 'QUIT':
			break
		if move in moves:
			#track_player(player)
			player = move_player(player, move)
			monster = move_monster(monster, value, moves_monster)
		elif move not in moves:
			print('Move not acceptable.')
			continue
		if player == door:
			print('You escaped. You Win!')
			break
		elif player == monster:
			print('You were eaten by the monster.You Lose.')
			break
		else:
			continue

if __name__ == '__main__':
	main()
