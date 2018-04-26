#!/usr/bin/env python3

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def talk(self):
		return 'Hello'
		#raise NotImplementedError('Subclass must implement abstract method')

class Dog(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)
	def talk(self):
		#raise NotImplementedError('Subclass must use own implementation of method')
		return 'Woof'
class Cat(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)
	def talk(self):
		return 'Meow'

def Main():
	peeps = [Dog('Bentley', 6), Cat('Josey', 4), Pet('Meow', 6)]
	'''
	print('My dog is my pet: ' + str(isinstance(my_dog, Pet)))
	print('My pet is my dog: ' + str(isinstance(my_pet, Dog)))
	print('My dog is my dog: ' + str(isinstance(my_dog, Dog)))
	print('My pet is my pet: ' + str(isinstance(my_pet, Pet)))
	'''
	for peep in peeps:
		print('Name: ' + str(peep.name) + ' Age: ' + str(peep.age) + ' Says: ' + str(peep.talk()))
	#print(my_dog.talk())
	#print(my_pet.talk())
if __name__ == '__main__':
	Main()
