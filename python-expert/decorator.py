#!/usr/bin/env python3

from time import time

def timer(func):
	def f(*args, **kwargs):
		before = time()
		rv = func(*args, **kwargs)
		after = time()
		print("elapsed: ", after-before)
		return rv
	return f

def ntimes(n):
	def inner(f):
		def wrapper(*args, **kwargs):
			for _ in range(n):
				print('running {.__name__}'.format(f))
				rv = f(*args, **kwargs)
			return rv
		return wrapper
	return inner

@ntimes(2)
def add(x, y=10):
	return x + y

@ntimes(5)
def sub(x, y=10):
	return x-y

@timer
def mul(x,y=10):
	return x*y

def main():
	print("Add (with ntimes decorator): ", add(2,3))
	print("Sub (with timer decorator): ", sub(2,3))
	print("Mul (with timer decorator): ", mul(2,3))
	
if __name__ == '__main__':
	main()