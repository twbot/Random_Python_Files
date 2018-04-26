#!/usr/bin/env python3

import random

CELLS = [(0,0), (0,1), (0,2),
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)]

PERSON = (0,1)
MONSTER = (0,0)

def draw_map(player, monster):
	print(' _ _ _ ')
	tile = '|{}'
	for index, cell in enumerate(CELLS):
		if index in [0, 1, 3, 4, 6, 7]:
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

def get_locations():
	door = random.choice(CELLS)
	person = random.choice(CELLS)
	monster = random.choice(CELLS)
	if (door == person) or (door == monster) or (monster == person):
		return get_locations()
	return door, person, monster

def move_player(player, move):
	x,y = player
	if move == 'LEFT':
		y -= 1
	elif move == 'RIGHT':
		y += 1
	elif move == 'UP':
		x -= 1
	elif move == 'DOWN':
		x += 1
	return x,y

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	if player[1] == 0:
		moves.remove('LEFT')
	if player[1] == 2:
		moves.remove('RIGHT')
	if player[0] == 0:
		moves.remove('UP')
	if player[0] == 2:
		moves.remove('DOWN')
	return moves


def main():
	door, person, monster = get_locations()
	index = 0
	print('Welcome to the dungeon.')
	while True:
		print('You are currently in position {}'.format(person))  #fill in with player position
		draw_map(PERSON, MONSTER)
		print('You can move {}'.format(moves))  #fill in with available moves
		print('Enter QUIT to quit.')
		move = input('>  ')
		move = move.upper()
		if move == 'QUIT':
			break
		if move in moves:
			person = move_player(person, move)
		elif move not in moves:
			print('Move not acceptable.')
			continue
		if person == door:
			print('You escaped. You Win!')
			break
		elif person == monster:
			print('You were eaten by the monster.You Lose.')
			break
		else:
			continue

if __name__ == '__main__':
	main()