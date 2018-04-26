#!/usr/bin/env python

import matplotlib.pyplot as plt
from sys import getsizeof


def check_for_highest_range(A):
	current_sum_left= 0
	current_sum_right = 0
	max_index_left = 0
	max_index_right = 0
	#keep track of max number on left side of array
	left_num = -(getsizeof(int))
	#keep track of max number on right side of array
	right_num = -(getsizeof(int))

	for price in reversed(A[:len(A)/2]):
		current_sum_left = current_sum_left + price
		if current_sum_left > left_num:
			left_num= current_sum_left
			max_index_left = price

	for price in A[(len(A)/2)+1:]:
		current_sum_right = current_sum_right+ price
		if current_sum_right > right_num:
			right_num= current_sum_right
			max_index_right = price

	return  A.index(max_index_left), A.index(max_index_right)

def create_plot(axis, stocks, growth, growth_axis):

	plot_stocks = plt.plot(axis, stocks, 'oc-')	#create stock chart
	plot_growth = plt.plot(growth_axis, growth,  'ob-')
	plt.plot(growth_axis[0], growth[0], color = 'green', marker = 'o', label = 'Buy')
	plt.plot(growth_axis[len(growth)-1], growth[len(growth)-1], 'ro', label = 'Sell')
	plt.xticks(axis)
	plt.setp(plot_stocks)
	plt.setp(plot_growth, linestyle = 'dashed')
	plt.xlabel('Day')
	plt.ylabel('Price')
	plt.title('Stock price over 17 days')
	plt.legend()
	plt.show()
	plt.close()

def main():
	stock_list = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
	delta_list = [stock_list[item+1]-stock_list[item] for item in range(len(stock_list)-1)]
	x_axis_stock = [i for i in range(len(stock_list))]
	
	index_left,index_right= check_for_highest_range(delta_list)
	x_value_left = index_left
	x_value_right = index_right+1

	growth = [stock for stock in stock_list[x_value_left:x_value_right+1]]
	x_axis_growth = [i for i in range(x_value_left, x_value_right+1)]
	
	create_plot(x_axis_stock, stock_list, growth, x_axis_growth)
	#y_value_left = stock_list[x_value_left]
	#y_value_right = stock_list[x_value_right]

	
	#plt.setp(sell)

if __name__ == '__main__':
	main()
