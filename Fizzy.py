#!/usr/bin/python

from __future__ import print_function

def main():
	i = 1
	for i in range(101):
		if int(i%3) == 0:
			print('Fizz')
			if int(i%5) == 0:
				print('Buzz')
		elif int(i%5) == 0:
			print('Buzz')
		else:
			print(i)


if __name__ == '__main__':
	main()