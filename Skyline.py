#!/usr/bin/env python
'''
	Takes a file of numbers containing list of integers,
'''

import os
import matplotlib.pyplot as plt

initial_skyline_list_x_axis = []
initial_skyline_list_y_axis = []


def clear_list(input_list):
	if len(input_list) != 0:
		for item in input_list:
			input_list.remove(item)
	return input_list

def draw_initial_skyline(list_of_tuples):
	for each_item in list_of_tuples:
		initial_skyline_list_x_axis.append(each_item[0])
		initial_skyline_list_x_axis.append(each_item[0])
		initial_skyline_list_x_axis.append(each_item[2])
		initial_skyline_list_x_axis.append(each_item[2])
		initial_skyline_list_y_axis.append(0)
		initial_skyline_list_y_axis.append(each_item[1]) 
		initial_skyline_list_y_axis.append(each_item[1]) 
		initial_skyline_list_y_axis.append(0)


def main():

	tuple_list = []	
	horizon_line = []	#instantiate output list

	current_dir = os.getcwd()
	file = open(os.path.join(current_dir, 'skyline_input.txt'), 'r')
	for line in file:
		tup = tuple(map(int,line.split()))	#map numbers to a 3-tuple
		tuple_list.append(tup)	#append tuple to skyline list

	draw_initial_skyline(tuple_list)
	
	skyline_init = plt.plot(initial_skyline_list_x_axis, initial_skyline_list_y_axis, 'g.-')
	plt.setp(skyline_init)
	plt.ylim(0, 35)
	plt.ylabel('Height')
	plt.xlabel('Width')
	plt.title('Skyline')
	plt.show()
	plt.close()
	
	start = tuple_list[0]	#variable to store first tuple occurence
	horizon_line.append(start[0])	#append li(left most point) to output list
	horizon_line.append(start[1])	#append hi(left most highest point) to output list

	for point in tuple_list[1:len(tuple_list)-1]:
		group = point[2]	#store right most point of next building
		next_lowest = point[1]
		index = tuple_list.index(point)+1
		for x in tuple_list[index:len(tuple_list)-1]:			 	
			if group in range(x[0], x[2]):
				if point[1] < x[1]:
					horizon_line.append(x[0])
					horizon_line.append(x[1])
					break
				elif point[1] > x[1]:
					horizon_line.append(group)
					horizon_line.append(x[1])
					break
			else:
				horizon_line.append(group)
				#append next lowest hight
				horizon_line.append(x[0])
				horizon_line.append(x[1])
				break

	print(horizon_line)
	#draw_modified_skyline(horizon_line)

	# skyline_mod = plt.plot(initial_skyline_list_x_axis, initial_skyline_list_y_axis, 'g.-')
	# plt.setp(skyline_init)
	# plt.ylim(0, 35)
	# plt.ylabel('Height')
	# plt.xlabel('Width')
	# plt.title('Skyline')
	# plt.show()
	# plt.close()

if __name__ == '__main__':
	main()