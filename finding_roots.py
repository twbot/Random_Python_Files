#!/usr/bin/env python3

'''
Roots Calculator

Find roots of numbers
up to the sixth root

'''

import argparse as ap
import re

def main():
	parser = ap.ArgumentParser(description='Usage: ./exe -n number -r root')
	parser.add_argument('-n', '--number', help = 'Number to find nth root of')
	parser.add_argument('-r', '--root', help= 'Number for root. (2-6)')
	

def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(newton_update(f, df, near_zero)


def newton_update():
	def update(x):
		return x-f(x) / df(x)
	return update


def improve(update, close, guess = 1, max=100):
	k = 0
	while not close(guess) and k < max:
		guess = update(guess):
		k = k+1
	return guess


def approx_eq(x, y, tolerance=1e-15):
	return abs(x-y) < tolerance


def square_root(a):
	return find_zero(lambda x: x*x-a, lambda x:2*x)

def cube_root(a):
	return find_zero(lambda x: x*x*x-a, lambda x: 3*x*x)

def fourth_root(a):
	return find_zero(lambda x: x*x*x*x-a, lambda x: 4*x*x*x)

def fifth_root(a):
	return find_zero(lambda x: x*x*x*x*x-a, lambda x: 5*x*x*x*x)
