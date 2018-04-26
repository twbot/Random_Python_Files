#!/usr/bin/env python3

'''
 Given a set S of n real numbers and another real number x, 
 determine whether or not there exists:
 	Two elements in S whose sum is exactly x.
 '''
 def find_sum_from_list():
 	x = int(input('Input number for which you wish to find sum: '))
	return_list = []
	s = list(map(int, input('Please input list of ints: ').split(',')))
	for integer in s:
		index = s.index(integer)
		new_s = s[index+1:] + s[:index]
		new_list = [(integer, num) for num in new_s if (integer+num) == x]
		if len(new_list) > 0:
			for tup in new_list:
				if tup not in return_list:
					return_list.append(tup)
	print(return_list)


def main():
	


if __name__ == '__main__':
	main()