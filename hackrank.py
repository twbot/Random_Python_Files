#!/usr/bin/python
import sys

"""def main():
	L = []
	for x in range(int(raw_input())):
    	s = raw_input().split()
    	if s[0] == 'insert':
        	L.insert(s[1], s[2])
    	elif s[0] == 'print':
        	print L
    	elif s[0] == 'remove':
        	L.remove(s[1])
    	elif s[0] == 'append':
        	L.append(s[1])
    	elif s[0] == 'sort':
        	L.sort()
    	elif s[0] == 'pop':
        	L.pop()
    	elif s[0] == 'reverse':
        	L.reverse()
"""
class vector2d():
	def __init__(self, x, y):
		self.x = x
		self.y = y

def main():
	vect = vector2d(5, 6)
	print 'X:', vect.x, ' Y:', vect.y

if __name__ == '__main__':
	main()