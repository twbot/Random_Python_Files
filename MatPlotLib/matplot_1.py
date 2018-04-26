#!/usr/bin/python

import matplotlib.pyplot as plt

def main():

	pop = [100, 20, 130, 95, 56, 46, 35, 24, 19, 103, 105, 67, 35, 34, 36, 75, 68, 94, 35, 24, 25, 26, 25, 27, 14, 9, 1, 23, 45, 36, 6, 7 ,43, 105]

	#plt.plot(x, y, label = 'FirstLine')
	#plt.plot(x2, y2, label = 'SecondLine')
	#plt.bar(x, y, label='bar1', color = 'g')
	#plt.bar(x2, y2, label='bar2', color = 'c')
	plt.hist(pop, bins=5, histtype = 'bar', color = 'c', rwidth = 0.8, label = 'Utopian Ages')
	plt.xlabel('Plot Number')
	plt.ylabel('Important var')
	plt.title('Awesome Graph')
	plt.legend()
	plt.show()

if __name__ == '__main__':
	main()