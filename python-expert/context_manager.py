#File to demonstrate context managers in python

from sqlite3 import connect
from contextlib import contextmanager

def main():
	choice = input('Choose either func, class,' +
			'generator, or context (contextmanager): ')

###########Original Database Creation###########
	if(choice == 'func'):
		with connect('test.db') as conn:
			cur = conn.cursor()
			cur.execute('create table points(x int, y int)')
			cur.execute('insert into points (x,y) values (1, 1)')
			cur.execute('insert into points (x,y) values (1, 2)')
			cur.execute('insert into points (x,y) values (2, 1)')
			for row in cur.execute('select x , y from points'):
				print(row)
			for row in cur.execute('select sum (x * y) from points'):
				print(row)
			cur.execute('drop table points')

###########Database Creation with Class###########
	if(choice == 'class'):
		class tempTable:
			def __init__(self, cur):
				self.cur = cur
			def __enter__(self):
				print('__enter__')
				self.cur.execute('create table points (x int, y int)')
			def __exit__(self, *args):
				print('__exit__')
				self.cur.execute('drop table points')

		with connect('test.db') as conn:
			cur = conn.cursor()
			with tempTable(cur):
				cur.execute('insert into points (x,y) values (1, 1)')
				cur.execute('insert into points (x,y) values (1, 2)')
				cur.execute('insert into points (x,y) values (2, 1)')
				for row in cur.execute('select x , y from points'):
					print(row)
				for row in cur.execute('select sum (x * y) from points'):
					print(row)

###########Database Creation with Generator###########
	if(choice == 'generator'):

		class contextManager:
			def __init__(self, gen):
				self.gen = gen
			def __call__(self, *args, **kwargs):
				self.args, self.kwargs = args, kwargs
				return self
			def __enter__(self, *args, **kwargs):
				self.gen_inst = self.gen(*self.args, **self.kwargs)
				next(self.gen_inst)
			def __exit__(self, *args):
				next(self.gen_inst, None)

		@contextManager
		def temptable(cur):
			print('created table')
			cur.execute('create table points (x int, y int)')
			yield
			cur.execute('drop table points')
			print('deleted table')

		#temptable = contextManager(temptable)

		with connect('test.db') as conn:
			cur = conn.cursor()
			with temptable(cur):
				cur.execute('insert into points (x,y) values (1, 1)')
				cur.execute('insert into points (x,y) values (1, 2)')
				cur.execute('insert into points (x,y) values (2, 1)')
				for row in cur.execute('select x , y from points'):
					print(row)
				for row in cur.execute('select sum (x * y) from points'):
					print(row)

###########Database Creation with ContextManager###########
	if(choice == "context"):
		
		@contextmanager
		def temptable(cur):
			print('created table')
			cur.execute('create table points (x int, y int)')
			try:
				yield
			finally:
				cur.execute('drop table points')
			print('deleted table')

		with connect('test.db') as conn:
			cur = conn.cursor()
			with temptable(cur):
				cur.execute('insert into points (x,y) values (1, 1)')
				cur.execute('insert into points (x,y) values (1, 2)')
				cur.execute('insert into points (x,y) values (2, 1)')
				for row in cur.execute('select x , y from points'):
					print(row)
				for row in cur.execute('select sum (x * y) from points'):
					print(row)

	else:
		raise NameError("No value found")
if __name__ == "__main__":
	main()
