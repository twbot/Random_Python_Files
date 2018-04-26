#!/usr/bin/env python3

import argparse
import os
import sys
#class argDef():

'''def __add__(a):
	b = 5
	result = a + b
	return result
	def fib(a):
		a, b = 0, 1
		for a*b 


def __div__( numer, denom):
	print numer//denom

def printy(stringy):
	print stringy
'''
def add_note(notes):
	return notes

def main():
	#args = sys.argv[1:]
	parser = argparse.ArgumentParser(description = 'Add a quick note.')
	parser.add_argument('-o', '--output', help = 'Output the result to file', action = 'store_true')
	parser.add_argument('note_str', help = 'Note to add', nargs='+')
	#parser.add_argument('num' , help = 'Input integer to add', type = int)
	#parser.add_argument('sec_num', help = 'Input second integer to be divided', type = int)
	#parser.add_argument('-d', '--divide', help = 'Divide the num by sec_num')
	

	note = parser.parse_args()
	notes = add_note(note.note_str)
	#result = __add__(name.num)
	#div = __div__(name.num, name.sec_num)
	#py = printy(name.p_print)
	directory = os.getcwd()
	notes_dir = os.path.join(directory, 'notes.txt')
	if note.output:
		if not(os.path.exists(notes_dir)):
			new_note = file('notes.txt', 'a')
		new_note.open(notes_dir, 'a')
		new_note.write(str(note.note_str)
			
if __name__ == '__main__':
	main()
