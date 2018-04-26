#!/usr/bin/env python3

import re
import os


class Person:
	def __init__(self, email, number,job, twitter):
		self.email = email
		self.number = number
		self.job = job
		self.twitter = twitter



def main():
	dict_of_individuals = {}

	current_directory = os.getcwd()
	directory = os.path.join(current_directory, 'names.txt')
	if not os.path.exists(directory):
		os.mkdir(directory)
	data = open(directory, 'r')
	data = data.read()

	matches = re.compile(r'''
		^(?P<name>[\w ]*,\s[\w\-]+)\t?\s?	#First and last names 
		(?P<email>[\w\d]*.?[\w\d]+@[\w.]+)?\t?	#Emails
		(?P<number>\(?\d{3}\)?\s?-?\d{3}-?\s?\d{4})?\t?	#Phone Numbers
		(?P<job>[\w ]*,\s[\w.? ?]+)?\t?	#Jobs
		(?P<twitter>@[\w\d]*)?\s?\t?$	#Twitter username
		''', re.X|re.M)

	for name in matches.finditer(data): 
		person_name = list(name.group('name').split(','))
		person_name = str(person_name[1]+ ' '+ person_name[0])
		person = Person(name.group('email'),name.group('number'),\
		 name.group('job'), name.group('twitter'))
		if not name in dict_of_individuals:
			dict_of_individuals[person_name] = person.email, \
			person.number, person.job, person.twitter

	for keys, values in dict_of_individuals.items():
		print('{0}: '.format(keys))
			#if email:
		print('Email: {}'.format(values[0]))
			#elif phone:
		print('Phone: {}'.format(values[1]))
			#elif job:
		print('Job: {}'.format(values[2]))
			#elif twitter:
		print('Twitter: {}'.format(values[3]))
		print('\n')

if __name__ == '__main__':
	main()