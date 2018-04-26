#!/usr/bin/env python3

# some behavior that I want to implement -> write some __ function __
# top-level function or top-level syntax -> corresponding __
# x + y -> __add__
# init x -> __init__
# repr(x) --> __repr__
# x() -> __call__

class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)

	def __add__(self, other):
		return Polynomial(*(x+y for x,y in zip(self.coeffs, other.coeffs)))

	def __len__(self):
		return len(self.coeffs)

	def __call__(self):
		pass


def main():
	poly1 = Polynomial(1,2,3)		#x²+2x+3
	poly2 = Polynomial(3,4,3)		#3x²+4x+3

if __name__ == '__main__':
	main()