#!/usr/bin/env python3

import re

def main():
	temperature = input('Please input a temperature; (e.g. 97.8 F, 36C): ')
	match = re.search(r'^([+-]?\s*[0-9]*(?:\.[0-9]*)?)\s*([C|F])\s*$', temperature, re.IGNORECASE)
	if match:
		degree = float(match.group(1))
		unit = match.group(2)
		if unit.lower() == 'c':
			fahrenheit = (degree * (9/5)) + 32
			print('{0} C is {1:.2f} F\n'.format(degree, fahrenheit))
		else:
			celcius= (degree - 32)* (5/9)
			print('{0} F is {1:.2f} C\n'.format(degree, celcius))
	else:
		print('Expecting a number followed by C or F')
		return main()


if __name__ == '__main__':
	main()