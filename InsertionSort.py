#!/usr/bin/env python3
import re
import sys
import os
import argparse

'''
# Method to count number of inversions in sorting method
def count_inversions(array):
'''

def insertion_sort(array):
	for index in range(1, len(array)):
		key = array[index]
		i = index - 1
		while i >= 0 and array[i] > key:
			array[i+1] = array[i]
			i -= 1
		array[i+1] = key
	return array

def reverse_insertion_sort(array):
	for index in range(1, len(array)):
		key = array[index]
		i = index - 1
		while i >= 0 and array[i] < key:
			array[i+1] = array[i]
			i = i -1
		array[i+1] = key
	return array


'''
def quick_sort(array):
	partition = array[len(array)/2]
	i = array[0]
	j = array[0]
	for j in array:
		if j < partition:
			tmp = 


def merge_sort(array):
	f_array = [: array/2]
	s_array = [(array/2)+1 :]
	

def count_pattern(pattern, string):
	i =0
	yes = re.search(pattern, string)
	if pattern in string:
		i += 1
	return i

def merge_sort(array):
	x = [:array/2]
	y = [array/2+1:]
'''

def main():
	hash_array = ['no', 'room', 'for', 'me', 'in', 'this', 'world']
	num_list = list(map(int,input('Please input integer array: ' ).split(',')))
	print('Unsorted list: {}'.format(num_list))
	print('Sorted list: {}'.format(reverse_insertion_sort(num_list)))
if __name__ == '__main__':
	main()