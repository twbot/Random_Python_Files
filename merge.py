#!/usr/bin/python

import sys
import os


"""def quicksort(array):
	i = array[0]
	j = array[i+1]
	back = array[(len(array)/2)+1:]
	
	if len(array) % 2  == 0:
		partition = array[len(array)/2]
	else:
		partition = array[(len(array)/2)-1]
	
	partition = array[0]
"""

def merge(array):
	if len(array) == 1:
		return array
	front = array[:len(array)/2]
	back = array[(len(array)/2)+1:]
	new_array= []
	proceed = 0
	i = 0
	j = 0
	for proceed in range(len(array-1)):
		if front[i] < back[j]:
			new_array[proceed] = back[j]
			i += 1
		elif back[j] < front[i]:
			new_array[proceed] = front[i]
			j += 1

	return new_array
def main():
	next = [3, 235, 453, 23, 234 ,4, 54, 4, 6, 9, 7,5 ,6, 85,6 , 6744, 5]
	print merge(next)

if __name__ == '__main__':
	main()