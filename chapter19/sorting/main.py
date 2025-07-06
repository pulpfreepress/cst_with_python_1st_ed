"""Demonstrate object equality."""

from person import Person
from datetime import datetime


def main():
	p1 = Person('Rick', 'W.', 'Miller', datetime(1996, 4, 27) )
	p2 = Person('David', 'W', 'Miller', datetime(1997, 12, 29))
	p3 = p1
	print(f'Is Rick the same age as David?: {p1 == p2}')
	print(f'Is p1 the same object as p2?: {p1 is p2}')
	print(f'Is p1 the same age as p3?: {p1 == p2}')
	print(f'Is p1 the same object as p3?: {p1 is p3}')



if __name__ == '__main__':
	main()