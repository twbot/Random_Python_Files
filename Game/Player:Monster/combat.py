#!/usr/bin/env python3
import random

class Combat():
	dodge_limit = 10
	attack_limit = 10
	def dodge(self):
		roll = random.randint(1, self.dodge_limit)
		return roll > 4
	def attack(self):
		roll = random.randint(1, self.attack_limit)
		return roll > 4
