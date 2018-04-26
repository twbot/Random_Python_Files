#File to demonstrate generators in python
#generators allow interweaving between user code and library code

#top-level syntax, function -> underscore_method
# x()									__call__

from time import sleep, time

def add1(x, y):
	return x+y

class Adder:
	def __call__(self, x, y):
		return x+y

add2 = Adder()
add1(2, 3)

#if you only care about a certain amount of data returned to rv
#or if you want to look at data one by one and toss it as it comes in
#you are unable to do so with this traditional approach
#takes up time and storage space if you only care about subset
#of the data space
def computeReg():
	rv = []
	a = time()
	for i in range(10):
		sleep(0.5)
		rv.append(i)
	b = time()
	print("Time {}".format(b-a))
	return rv

#what happens when for x in xr is called?
# -->		xi = iter(xs)		-> __iter__
#			while True:
#				x= next(xi)		-> __next__
# can use dunder methods to iterate through one by one
class Compute:
	def __iter__(self):
		self.last = 0
		return self
	def __next__(self):
		rv = self.last
		self.last += 1
		if self.last > 10:
			raise StopIteration()
		sleep(0.5)
		return rv

def runCompute():
	before = time()
	for val in Compute():
		val+=2
		print(val)
	after = time()
	print("Time {}".format(after-before))


def computeGen():
	for i in range(10):
		sleep(0.5)
		yield i

def runGen():
	before = time()
	for val in computeGen():
		val = val**2
		print(val)
	after = time()
	print("Time {}".format(after-before))

