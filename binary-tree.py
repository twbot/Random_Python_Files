#!/usr/bin/env python3

from queue import Queue


class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left_node = None
		self.right_node = None

	def insert_left(self, value):
		if self.left_node == None:
			self.left_node = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.left_node = self.left_node
			self.left_node = new_node

	def insert_right(self, value):
		if self.right_node == None:
			self.right_node = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.right_node = self.right_node
			self.right_node = new_node

	def bfs(self):
		queue = Queue()
		queue.put(self)

		while not queue.empty():
			current_node = queue.get()
			print(current_node.value)

			if current_node.left_node:
				queue.put(current_node.left_node)

			if current_node.right_node:
				queue.put(current_node.right_node)


def BinarySearchTree(self):
	
	def __init__(self, value):
		self.value = value
		self.left_node = None
		self.right_node = None

	def insert_node(self, value):
		if(value <= self.value and self.left_node):
			self.left_node.insert_node(value)
		elif(value <= self.value):
			self.left_node = BinarySearchTree(value)
		elif(value > self.value and self.right_node):
			self.right_node.insert_node(value)
		else:
			self.right_node = BinarySearchTree(value)

	def find_node(self, value):
		if(value < self.value and self.left_node):
			self.left_node.find_node(value)
		elif(value > self.value and self.right_node):
			self.right_node.find_node(value)

		return value == self.value

	def remove_node(self, value, parent):
		if (value < self.value and self.left_node):
			return self.left_node.remove_node(value, self)
		elif (value < self.value):
			return False
		elif (value > self.value and self.right_node):
			return self.right_node.remove_node(value, self)
		elif (value > self.value):
			return False
		else:
			if (self.left_node is None and self.right_node is None and self == parent.left_node):
				parent.left_node = None
				self.clear_node()
			elif (self.left_node is None and self.right_node is None and self == parent.right_node):
				parent.right_node = None
				self.clear_node()
			elif (self.left_node and self.right_node is None and self == parent.left_node):
				parent.left_node = self.left_node
				self.clear_node()
			elif (self.left_node and self.right_node is None and self == parent.right_node):
				parent.right_node = self.left_node
				self.clear_node()
			elif (self.right_node and self.left_node is None and self == parent.left_node):
				parent.left_node = self.right_node
				self.clear_node()
			elif (self.right_node and self.left_node is None and self == parent.right_node):
				parent.right_node = self.right_node
				self.clear_node()
			else:
				self.value = self.right_node.find_minimum_node()
				self.right_node.remove_node(self.value, self)

			return True

	def clear_node(self):
		self.value = None
		self.left_node = None
		self.right_node = None

	def find_minimum_node(self):
		if self.left_node:
			return self.left_node.find_minimum_node()
		else:
			return self.value



def printBinaryTree():
	a_tree = BinaryTree('a')
	print(a_tree.value)
	print(a_tree.left_node)
	print(a_tree.right_node)

	a_tree.insert_left('b')
	b_tree = a_tree.left_node
	b_tree.insert_right('d')

	a_tree.insert_right('c')
	c_tree = a_tree.right_node
	c_tree.insert_right('f')
	c_tree.insert_left('e')

	print("A: Left: " + a_tree.left_node.value)
	print("A: Right: " + a_tree.right_node.value)
	print("B: Right: " + b_tree.right_node.value)
	print("C: Left: " + c_tree.left_node.value)
	print("C: Right: " + c_tree.right_node.value)

	a_tree.bfs()

def printBinarySearchTree():
	bst = BinarySearchTree(15)
	bst.insert_node(10)
	bst.insert_node(8)
	bst.insert_node(12)
	bst.insert_node(20)
	bst.insert_node(17)
	bst.insert_node(25)
	bst.insert_node(19)
	print(bst.find_node(15))
	print(bst.find_node(10))
	print(bst.find_node(8))
	print(bst.find_node(12))
	print(bst.find_node(20))
	print(bst.find_node(17))
	print(bst.find_node(25))
	print(bst.find_node(19))
	print(bst.remove_node(8, None)) # True
	print(bst.remove_node(17, None)) # True
	print(bst.remove_node(15, None)) # True
	
def main():
	printBinarySearchTree()

if __name__ == '__main__':
	main()