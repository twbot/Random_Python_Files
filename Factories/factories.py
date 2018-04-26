#!/usr/bin/env python3

BaseClass = type('BaseClass', (), {})

@classmethod
def check1(cls, string):
	return string == 'one'

@classmethod
def check2(cls, string):
	return string == 'two'

foo = type('Class1', (BaseClass,), {'x': 'one', 'Check': check1})
bar = type('Class2', (BaseClass,), {'x': 'one', 'Check': check2})

def MyFactory():
	for cls in BaseClass.__subclasses__():
		if cls.Check(cls.x):
			return cls()

if __name__ == '__main__':
	MyFactory()