#!/usr/bin/env python3

class Singleton():
	hello = None
	def __new__(self):
		if not self.hello:
			self.hello = super(Singleton, self).__new__(self)
			self.y = 10
		return self.hello
	def __init__(self):
		self.y = 10

def main():
	new = Singleton()
	print(new.y)
	new.y = 20
	z = Singleton()
	print(z.y)
	z.y = 20	

if __name__ == '__main__':
	main()