#!/usr/bin/env python3

class Shapes:
	def __init__(self, name, points):
		self.name = name
		self.points = points
	def describe(self):
		raise NotImplementedError('Must use subclass for describe method')
class Triangle(Shapes):
	def __init__(self, name, points):
		super().__init__('Triangle', 3)
	def describe():
		return 'I am a ' + str(self.name) + ' and have ' + str(self.points) + ' points'
class Square(Shapes):
	def __init__(self, name, points):
		super().__init__(name, points)
	def describe():
		return 'I am a ' + str(self.name) + ' and have ' + str(self.points) + ' points'
class Circle(Shapes):
	def __init__(self, name, points):
		super().__init__('Circle', 0)
	def describe():
		return 'I am a ' + str(self.name) + ' and have ' + str(self.points) + ' points'
class Hexagon(Shapes):
	def __init__(self, name, points):
		super().__init__('Hexagon', 6)
	def describe():
		return 'I am a ' + str(self.name) + ' and have ' + str(self.points) + ' points'
class Pentagon(Shapes):
	def __init__(self, name, points):
		super().__init__('Pentagon', 5)
	def describe():
		return 'I am a ' + str(self.name) + ' and have ' + str(self.points) + ' points'
def main():
	shapes = [Triangle, Circle, Hexagon, Square, Pentagon]
	for shape in shapes:
		print(shape.describe())

if __name__ == '__main__':
	main()