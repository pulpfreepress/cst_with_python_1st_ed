"""Demonstrate object equality."""

from person import Person
from datetime import datetime


def main():
	p1 = Person('Rick', 'W', 'Miller', datetime(1996, 4, 27) )
	p2 = Person('David', 'W', 'Miller', datetime(1997, 12, 29))
	p3 = Person('Coralie', 'S', 'Miller', datetime(1999, 8, 9))
	people = [p1, p2, p3]
	sorted_people = sorted(people)

	print('Before Sort:')
	for p in people:
		print(f'{p.full_name_and_age}')
	
	print('After Sort:')
	for p in sorted_people:
		print(f'{p.full_name_and_age}')


if __name__ == '__main__':
	main()