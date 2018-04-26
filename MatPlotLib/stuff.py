#!/usr/bin/env python

import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7]
x1 = [8,9,10,11]
y = [0,1,2,3,5,6,7,8]
y1 = [9,10,11,12]
x2 = [2,23,45,68]

def main():
	plt.plot(x, y, 'go-', label = 'Test1', antialiased = False)
	lines = plt.plot(x1,y1, 'b*-', label = 'Test2')
	plt.setp(lines)
	plt.xlabel('Testx')
	plt.ylabel('Testy')
	plt.axis([0,15,0,15])
	plt.legend()
	plt.show()
	plt.close()

if __name__ == '__main__':
	main()