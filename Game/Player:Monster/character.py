#!/usr/bin/env python3

from combat import Combat
import random

class Character(Combat):
	experience = 6
	attack_limit = 10
	dodge_limit = 10
	hit_points = 6
	base_hit_points = 10

	def attack(self):
		roll = random.randint(1, self.attack_limit)
		if self.weapon == 'Sword':
			roll += 2
		elif self.weapon == 'Axe':
			roll += 1
		print(roll)
		return roll > 4 

	def get_weapon(self):
		weapon = input('Choose weapon: (S)word, (A)xe, (B)at: ')
		weapon = weapon.lower()
		if weapon in 'sab':
			if weapon == 's':
				return 'Sword'
			elif weapon == 'a':
				return 'Axe'
			elif weapon == 'b':
				return 'Bat'
		else:
			print('Weapon not available. Please choose the ones listed')
			return self.get_weapon()

	def __init__(self, **kwargs):
		self.name = input('Name: ')
		self.weapon = self.get_weapon()
		self.hit_points = self.base_hit_points

	def __str__(self):
		return '{}, Weapon: {}, HP: {}, XP: {}'.format(self.name, self.weapon, self.hit_points, self.experience)
		