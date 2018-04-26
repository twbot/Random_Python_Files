#!/usr/bin/env python3

import re
import os


def main():
	#list_people = []
	directory = os.path.join(os.getcwd(), 'names.txt')
	if not os.path.exists(directory):
		os.mkdir(directory)
	file = open(directory, 'r')
	data = file.read()
	people = re.compile(r'''
		^(?P<name>[\w ]*,\s[\w\-]+)\t?\s?	#First and last names 
		(?P<email>[\w\d]*.?[\w\d]+@[\w.]+)?\t?	#Emails
		(?P<number>\(?\d{3}\)?\s?-?\d{3}-?\s?\d{4})?\t?	#Phone Numbers
		(?P<job>[\w ]*,\s[\w.? ]+)?\t?	#Jobs
		(?P<twitter>@[\w\d]*)?\s?\t?$	#Twitter username
		''', re.X|re.M)

	for index in people.finditer(data):
		for x in index.groupdict():
			print(index.group(x))


if __name__ == '__main__':
	main()